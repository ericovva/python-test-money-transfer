from django.core.management.base import BaseCommand, CommandError
from account.models import Account
from payment.models import Payment
import uuid

class Command(BaseCommand):
    help = 'Create accounts'

    def handle(self, *args, **options):
        if len(Account.objects.all()):
            return

        for cur in Account.Currencies:
            acc1 = Account.objects.create(id=uuid.uuid4(), currency=cur[0], balance=0)
            acc2 = Account.objects.create(id=uuid.uuid4(), currency=cur[0], balance=0)
            Payment.objects.create(account=acc1, to_account=acc1, amount=123.12, direction=Payment.INCOMING)
            acc1.balance = Payment.recalc_account_balance(acc1.id)
            acc1.save()

