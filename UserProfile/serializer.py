from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'display_name','bio']