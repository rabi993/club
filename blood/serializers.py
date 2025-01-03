from rest_framework import serializers
from .models import Blood
from django.contrib.auth.models import User
from .models import People

class BloodSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    blood_group = serializers.CharField(source='person.blood_group', read_only=True)

    class Meta:
        model = Blood
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'blood_group',
            'last_donate_date',
        ]

