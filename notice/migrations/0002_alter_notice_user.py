# Generated by Django 4.2.16 on 2025-01-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
