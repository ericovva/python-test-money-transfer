"""API exceptions for payment app"""
from rest_framework.exceptions import APIException

class CurrenciesNotMatched(APIException):
    """If account currencies are not same"""
    status_code = 400
    default_detail = "Account currencies don't match."
    default_code = 'currencies_not_matched'


class InvalidAccounts(APIException):
    """If transfer between same accounts"""
    status_code = 400
    default_detail = "Invalid accounts"
    default_code = 'invalid_accounts'


class NotEnoughMoney(APIException):
    """If not enough money on account"""
    status_code = 400
    default_detail = "Not enough money"
    default_code = 'not_enough_money'
