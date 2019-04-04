"""Models account"""
from django.db import models

class Account(models.Model):
    """Model account"""
    USD = 'USD'
    RUB = 'RUB'

    Currencies = (
        (USD, 'United States Dollar'),
        (RUB, 'Russian Ruble'),
    )
    id = models.CharField(max_length=100, primary_key=True)
    balance = models.DecimalField(max_digits=100, decimal_places=2)
    currency = models.CharField(max_length=10, choices=Currencies)

    def __str__(self):
        return '{}: {} {}'.format(self.id, self.balance, self.currency)
