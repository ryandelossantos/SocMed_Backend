from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from .models import Post, Comment, Like
from .serializer import PostSerializer, CommentSerializer, LikeSerializer, GetPostSerializer
from django.contrib.auth.models import User

class PostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.annotate(
            comments_count=Count('comments'),
            likes_count=Count('likes')
        ).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostLikeAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if Like.objects.filter(post=post, user=request.user).exists():
            return Response({"detail": "Already liked this post"}, status=status.HTTP_400_BAD_REQUEST)
        Like.objects.create(post=post, user=request.user)
        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)

class PostCommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        content = request.data.get('content')
        if not content:
            return Response({"detail": "Content is required"}, status=status.HTTP_400_BAD_REQUEST)
        Comment.objects.create(post=post, user=request.user, content=content)
        return Response({"detail": "Comment added"}, status=status.HTTP_201_CREATED)

class CommentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        comments = Comment.objects.all().order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, post=post)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

class LikeListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
            if Like.objects.filter(post=post, user=request.user).exists():
                return Response({"detail": "Already liked this post"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = LikeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, post=post)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
