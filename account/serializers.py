from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    
    account_no = serializers.CharField(read_only=True)  # Prevent changes to account_no
    final_cash = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)  # Read-only field

    class Meta:
        model = Account
        fields = ['id', 'account_no', 'total_credit', 'total_debit', 'final_cash', 'created_at', 'updated_at']
        read_only_fields = ['final_cash', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        """
        Override the update method to ensure final_cash is recalculated.
        """
        instance.total_credit = validated_data.get('total_credit', instance.total_credit)
        instance.total_debit = validated_data.get('total_debit', instance.total_debit)
        instance.update_final_cash()  # Recalculate the final cash
        return instance
