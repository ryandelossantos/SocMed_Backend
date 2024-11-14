from rest_framework import serializers
from UserProfile.models import UserProfile
from .models import Post, Comment, Like

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'display_name', 'avatar', 'bio']

class PostSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'updated_at', 'image', 'comments_count', 'likes_count']

class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']
