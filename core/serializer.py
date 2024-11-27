from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth.models import User
from UserProfile.models import UserProfile
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class UserProfileSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = UserProfile 
        fields = ['avatar']

class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id' , 'email' , 'username' , 'password' , 'password_confirmation']
        # extra_kwargs = {
        #     'password': {'write_only': True},
        # }

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password_confirmation']:
            raise serializers.ValidationError('Password does not match.')
        validated_data.pop('password_confirmation')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if validated_data['password'] != validated_data['password_confirmation']:
            raise serializers.ValidationError('Password does not match.')
        validated_data.pop('password_confirmation')
        return super().update(instance, validated_data)