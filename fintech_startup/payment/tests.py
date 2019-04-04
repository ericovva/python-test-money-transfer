"""Tests for payment"""
import uuid
from rest_framework.test import APIClient

from django.test import TestCase
from account.models import Account
from payment.models import Payment

class PaymentTestCase(TestCase):
    """Test cases for checking transfer process"""
    def __init__(self, *argv, **kw):
        self.id1 = uuid.uuid4()
        self.id2 = uuid.uuid4()
        self.id3 = uuid.uuid4()
        super().__init__(*argv, **kw)

    def setUp(self):
        acc1 = Account.objects.create(id=self.id1, balance=0, currency=Account.USD)
        Payment.objects.create(
            account=acc1,
            to_account=acc1,
            direction=Payment.INCOMING,
            amount=100
        )
        Account.objects.create(id=self.id2, balance=0, currency=Account.USD)
        Account.objects.create(id=self.id3, balance=0, currency=Account.RUB)

    def test_success_payment(self):
        """Test success payment"""
        client = APIClient()
        cli = client.post('/payment', {
            'amount': 10,
            'account': self.id1,
            'to_account': self.id2
        }, format='json')
        self.assertEqual(cli.status_code, 201)

        acc1 = Account.objects.get(id=self.id1)
        acc2 = Account.objects.get(id=self.id2)
        self.assertEqual(acc1.balance, 90)
        self.assertEqual(acc2.balance, 10)

    def test_fail_payment_negative_amount(self):
        """Test fail payment"""
        client = APIClient()
        cli = client.post('/payment', {
            'amount': -10,
            'account': self.id1,
            'to_account': self.id2
        }, format='json')
        self.assertEqual(cli.status_code, 400)

    def test_fail_payment_negative_balance(self):
        """Test fail payment"""
        client = APIClient()
        cli = client.post('/payment', {
            'amount': 110,
            'account': self.id1,
            'to_account': self.id2
        }, format='json')
        self.assertEqual(cli.status_code, 400)

    def test_fail_payment_incorrect_currencies(self):
        """Test fail payment"""
        client = APIClient()
        cli = client.post('/payment', {
            'amount': 50,
            'account': self.id1,
            'to_account': self.id3
        }, format='json')
        self.assertEqual(cli.status_code, 400)

    def test_fail_payment_account_invalid_pk(self):
        """Test fail payment"""
        client = APIClient()
        cli = client.post('/payment', {
            'amount': 50,
            'account': self.id1,
            'to_account': 'abc'
        }, format='json')
        self.assertEqual(cli.status_code, 400)

    def test_fail_payment_account_accounts(self):
        """Test fail payment"""
        client = APIClient()
        cli = client.post('/payment', {
            'amount': 50,
            'account': self.id1,
            'to_account': self.id1
        }, format='json')
        self.assertEqual(cli.status_code, 400)

    def test_fail_payment_account_invalid_params(self):
        """Test incorrect arguments"""
        client = APIClient()
        cli = client.post('/payment', {
            'amount': None,
            'account': self.id1,
            'to_account': self.id2
        }, format='json')
        self.assertEqual(cli.status_code, 400)
        cli = client.post('/payment', {
            'amount': 50,
            'account': None,
            'to_account': self.id2
        }, format='json')
        self.assertEqual(cli.status_code, 400)
        cli = client.post('/payment', {
            'amount': 50,
            'account': self.id1,
            'to_account': None
        }, format='json')
        self.assertEqual(cli.status_code, 400)
