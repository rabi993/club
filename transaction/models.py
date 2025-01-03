from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from account.models import Account  # Ensure no circular imports

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)  # Link transaction to an account
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')  # Link transaction to a user
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

    # def update_account(self):
    #     """
    #     Updates the associated account's total_credit, total_debit, and final_cash.
    #     """
    #     if self.typys == 'credit':
    #         self.account.total_credit += self.amount
    #     elif self.typys == 'debit':
    #         self.account.total_debit += self.amount

    #     # Update final cash and save
    #     self.account.update_final_cash()




# @receiver(post_save, sender=Transaction)
# def update_account_on_transaction(sender, instance, created, **kwargs):
    
#     instance.update_account()
    def update_account_on_create(self):
        """
        Update the account when a transaction is created.
        """
        if self.typys == 'credit':
            self.account.total_credit += self.amount
        elif self.typys == 'debit':
            self.account.total_debit += self.amount
        self.account.update_final_cash()

    def update_account_on_edit(self, old_amount, old_typys):
        """
        Update the account when a transaction is edited.
        """
        if old_typys == 'credit':
            self.account.total_credit -= old_amount
        elif old_typys == 'debit':
            self.account.total_debit -= old_amount

        if self.typys == 'credit':
            self.account.total_credit += self.amount
        elif self.typys == 'debit':
            self.account.total_debit += self.amount

        self.account.update_final_cash()

    def update_account_on_delete(self):
        """
        Update the account when a transaction is deleted.
        """
        if self.typys == 'credit':
            self.account.total_credit -= self.amount
        elif self.typys == 'debit':
            self.account.total_debit -= self.amount
        self.account.update_final_cash()


@receiver(pre_save, sender=Transaction)
def handle_transaction_update(sender, instance, **kwargs):
    """
    Handles updates to a transaction.
    """
    if instance.pk:  # Only if the transaction already exists (i.e., edit mode)
        old_transaction = Transaction.objects.get(pk=instance.pk)
        instance.update_account_on_edit(old_transaction.amount, old_transaction.typys)


@receiver(post_save, sender=Transaction)
def handle_transaction_create(sender, instance, created, **kwargs):
    """
    Handles creating a new transaction.
    """
    if created:  # Only if the transaction is newly created
        instance.update_account_on_create()


@receiver(models.signals.post_delete, sender=Transaction)
def handle_transaction_delete(sender, instance, **kwargs):
    """
    Handles deleting a transaction.
    """
    instance.update_account_on_delete()