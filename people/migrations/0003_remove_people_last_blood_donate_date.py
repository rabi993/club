# Generated by Django 4.2.16 on 2025-01-05 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_people_birth_date_people_last_blood_donate_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='last_blood_donate_date',
        ),
    ]
