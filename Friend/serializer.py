from rest_framework import serializers
from UserProfile.serializer import UserProfileSerializer
from .models import Friendship

class FriendshipSerializer(serializers.ModelSerializer):
    user_1 = UserProfileSerializer(read_only=True)
    user_2 = UserProfileSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ['id', 'user_1', 'user_2', 'status', 'created_at']