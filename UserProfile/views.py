from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser

from .models import UserProfile

class UserProfileView(APIView):
    
    def get(self ,request ,  format=None):
        users = User.objects.all()
        serializer = UserProfileSerializer(users , many=True)
        return Response({'ok': True , 'data': serializer.data} , status=200)

    def post(self , request , format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()

            return Response({'ok': True , 'data' : serializer.data} , status=200)
        return Response({'ok': False , 'errors': serializer.errors},status=400)
    

    def patch(self , request , format=None):
        try:
            user_instance = User.objects.get(id=request.data['id'])
            if user_instance.check_password(request.data['old_password']):
                request.data.pop('old_password')
                serializer = UserProfileSerializer(user_instance , data=request.data ,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    user = User.objects.get(id=request.data['id'])
                    user.set_password(request.data['password'])
                    user.save()
                    return Response({'ok': True , 'message': 'Password Changed Successful.'}, status=200)
                return Response({'ok': False , 'errors': serializer.errors}, status=400)
            return Response({'ok': False , 'messae' : 'Old password is invalid.'})
        except:
            return Response({'ok': False , 'message': 'user not exist.'},status=404)
    
    def delete(self, request , format=None):
        req_data = JSONParser().parse(request)

        object_instance = UserProfile.objects.get(id=req_data['id'])

        object_instance.delete()

        return Response("deleted!")