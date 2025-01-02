from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class NoticeViewset(viewsets.ModelViewSet):
    queryset = models.Notice.objects.all()
    serializer_class = serializers.NoticeSerializer


