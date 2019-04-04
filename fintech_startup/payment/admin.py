"""Admin interface for creating/deleting/updating payments for test"""
from django.contrib import admin
from payment.models import Payment

class PaymentAdmin(admin.ModelAdmin):
    """Accounts admin custom class"""
    list_display = (
        'id',
        'account',
        'amount',
        'to_account',
        'direction',
        'tr_hash',
    )
    search_fields = ('id', 'account__id', 'to_account__id', 'tr_hash',)

admin.site.register(Payment, PaymentAdmin)
