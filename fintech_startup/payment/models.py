"""Models payment"""
import uuid
from django.db import models
from account.models import Account

class Payment(models.Model):
    """Model payment"""
    OUTGOING = -1
    INCOMING = 1

    Directions = (
        (OUTGOING, 'outgoing'),
        (INCOMING, 'incoming'),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accounts')
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='to_accounts')
    direction = models.IntegerField(choices=Directions)
    tr_hash = models.UUIDField(default=uuid.uuid4())

    @classmethod
    def recalc_account_balance(cls, account_id):
        """Recount balance of account"""
        amounts = cls.objects.filter(
            account=account_id,
        ).aggregate(
            _in=models.Sum('amount', filter=models.Q(direction=cls.INCOMING)),
            _out=models.Sum('amount', filter=models.Q(direction=cls.OUTGOING))
        )
        return (amounts['_in'] or 0) - (amounts['_out'] or 0)
