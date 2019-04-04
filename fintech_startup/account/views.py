"""API endpoint classes for account app"""
from rest_framework.viewsets import ModelViewSet
from account import serializers as account_serializers
from account import models as account_models


class Account(ModelViewSet):
    """Endpoint class for account"""
    queryset = account_models.Account.objects.all()
    serializer_class = account_serializers.AccountSer
    http_method_names = ['get']
