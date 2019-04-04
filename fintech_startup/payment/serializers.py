"""Serializers payment"""
from rest_framework import serializers
from payment.models import Payment


class PaymentSer(serializers.ModelSerializer):
    """Serializer payment"""
    @staticmethod
    def validate_amount(value):
        """Additional checking amount"""
        if value < 0:
            raise serializers.ValidationError('Amount less than zero')
        return value

    class Meta:
        """Meta description"""
        model = Payment
        fields = '__all__'
        read_only_fields = ('direction', 'tr_hash',)
