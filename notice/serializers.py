import requests
from rest_framework import serializers
from . import models

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notice
        fields = '__all__'
    


from . import models
class CommentSerializer(serializers.ModelSerializer):
    # commentor = serializers.CharField(source='commentor.first_name', read_only=True)  # Corrected
    # post = serializers.CharField(source='post.title', read_only=True)  # Corrected

    class Meta:
        model = models.noticeComment
        fields = '__all__'

    