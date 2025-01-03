# Generated by Django 4.2.16 on 2025-01-03 01:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(default=uuid.uuid4, max_length=20, unique=True)),
                ('total_credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total_debit', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('final_cash', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'ordering': ['-created_at'],
            },
        ),
    ]
