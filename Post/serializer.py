from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'media', 'created_at', 'updated_at', 'comments_count', 'likes_count','comments']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']


class GetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'media', 'created_at', 'updated_at']