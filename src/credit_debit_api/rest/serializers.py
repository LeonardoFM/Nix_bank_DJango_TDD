from rest_framework import serializers

from credit_debit_api.models import Transaction, VirtualAccount

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('description','balance','debit','credit','status','date')

class VirtualAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualAccount
        fields = ('name','agency','current_account')