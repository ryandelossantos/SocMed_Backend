from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment
from .serializer import PostSerializer , CommentSerializer
class PostView(APIView):
    def get(self , request , format=None):
        
        all_post = Post.objects.all().order_by('-id')
        serializer = PostSerializer(all_post , many=True)
        return Response({'ok': True , 'data': serializer.data})
    

class AddCommentView(APIView):
    def post(self , request , format=None):
        serializer = CommentSerializer(data={"created_by": 1 , **request.data})
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data})
        return Response({'ok': False , 'error': serializer.errors})