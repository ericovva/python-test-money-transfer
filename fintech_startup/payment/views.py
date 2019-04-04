"""API endpoint classes for payment app"""
import uuid
from django.db import transaction
from bulk_update.helper import bulk_update

from rest_framework.viewsets import ModelViewSet

from payment import serializers as payment_serializers
from payment import exceptions
from payment import models as payment_models
from account import models as account_models


class Payment(ModelViewSet):
    """Endpoint class for payment"""
    queryset = payment_models.Payment.objects.select_related()
    serializer_class = payment_serializers.PaymentSer
    http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        """Make transaction"""
        data = serializer.data
        with transaction.atomic():
            accounts = {
                acc.id : acc for acc in account_models.Account.objects.select_for_update().filter(
                    id__in=(data['account'], data['to_account'])
                )
            }
            if len(accounts) != 2:
                raise exceptions.InvalidAccounts

            account = accounts[data['account']]
            to_account = accounts[data['to_account']]

            if account.currency != to_account.currency:
                raise exceptions.CurrenciesNotMatched

            tr_hash = uuid.uuid4()
            payment_models.Payment.objects.bulk_create([
                payment_models.Payment(
                    account=account,
                    amount=data['amount'],
                    to_account=to_account,
                    direction=payment_models.Payment.OUTGOING,
                    tr_hash=tr_hash
                ),
                payment_models.Payment(
                    account=to_account,
                    amount=data['amount'],
                    to_account=account,
                    direction=payment_models.Payment.INCOMING,
                    tr_hash=tr_hash
                )
            ])

            account.balance = payment_models.Payment.recalc_account_balance(account.id)
            to_account.balance = payment_models.Payment.recalc_account_balance(to_account.id)

            if account.balance < 0:
                raise exceptions.NotEnoughMoney

            bulk_update([account, to_account])
