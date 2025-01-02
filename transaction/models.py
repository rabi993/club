from django.db import models
from django.contrib.auth.models import User  # Assuming you use Django's built-in User model

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')  # Link to the user making the transaction
    trx_id = models.CharField(max_length=255, unique=True)  # Unique transaction ID
    reference = models.CharField(max_length=255, blank=True, null=True)  # Reference (optional)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    typys = models.CharField(max_length=10, choices=TYPES)  # Transaction type (credit or debit)
    source_people = models.CharField(max_length=255, blank=True, null=True)  # Source or recipient of funds
    media = models.CharField(max_length=255, blank=True, null=True)  # Payment method or medium
    purpose = models.TextField(blank=True, null=True)  # Purpose of the transaction
    comment = models.TextField(blank=True, null=True)  # Additional comments
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of transaction creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of last update

    def __str__(self):
        return f"Transaction {self.trx_id} by {self.user.username}"
