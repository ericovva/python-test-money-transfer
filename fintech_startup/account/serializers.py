"""Serializers account"""
from rest_framework import serializers
from account.models import Account


class AccountSer(serializers.ModelSerializer):
    """Serializer account"""
    class Meta:
        """Meta description"""
        model = Account
        fields = '__all__'
