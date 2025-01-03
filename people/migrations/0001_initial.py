# Generated by Django 4.2.16 on 2025-01-03 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, max_length=500, null=True)),
                ('mobile_no', models.CharField(max_length=15)),
                ('union', models.CharField(blank=True, max_length=255, null=True)),
                ('word', models.CharField(blank=True, max_length=255, null=True)),
                ('village', models.CharField(blank=True, max_length=255, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Separated', 'Separated'), ('Divorced', 'Divorced')], max_length=10, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('worksat', models.CharField(blank=True, max_length=255, null=True)),
                ('livesIn', models.CharField(blank=True, max_length=255, null=True)),
                ('varsity', models.CharField(blank=True, max_length=255, null=True)),
                ('session', models.CharField(blank=True, max_length=20, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('association_post', models.CharField(blank=True, max_length=255, null=True)),
                ('cv', models.URLField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
    ]
