from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserProfileSerializer

from rest_framework.parsers import JSONParser

from .models import UserProfile

class UserProfileView(APIView):
    
    def get(self , request , format=None):
        data = UserProfile.objects.all().order_by('-id')
        serializer = UserProfileSerializer(data , many=True)
        return Response({'ok': True, 'data': serializer.data} , status=200)
    
    def post(self , request , format=None):
        # data = JSONParser().parse(request)

        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data}, status=200)
        
        return Response({'ok': False , 'message': 'something went wrong!'})
    
    def patch(self , request , format=None):
        # req_data = JSONParser().parse(request)

        object_instance = UserProfile.objects.get(id=req_data['id'])
        print(object_instance)

        serializer = UserProfileSerializer(object_instance , data=req_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'data': serializer.data}, status=200)
        
        return Response({'ok': False, 'message': 'something went wrong'})
    
    def delete(self, request , format=None):
        req_data = JSONParser().parse(request)

        object_instance = UserProfile.objects.get(id=req_data['id'])

        object_instance.delete()

        return Response("deleted!")