from rest_framework import serializers
from .models import Post
from category.models import Category

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False, read_only=True)  # Display user as a string (e.g., username)
    
    # Show category names while allowing edits via IDs
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',  # Use the name field for display
        many=True
    )
    

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': True},
            'content': {'required': True},
            'image': {'required': True},
            
        }




from . import models
class CommentSerializer(serializers.ModelSerializer):
    # commentor = serializers.CharField(source='commentor.first_name', read_only=True)  # Corrected
    # post = serializers.CharField(source='post.title', read_only=True)  # Corrected

    class Meta:
        model = models.Comment
        fields = '__all__'

    