from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Count
from .models import Post, Comment, Like
from .serializer import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.annotate(
        comments_count=Count('comments'),
        likes_count=Count('likes')
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'update' or self.action == 'partial_update':
            return [IsAuthenticatedOrReadOnly()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this post.")
        serializer.save()

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        if Like.objects.filter(post=post, user=request.user).exists():
            return Response({"detail": "Already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(post=post, user=request.user)
        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        post = self.get_object()
        content = request.data.get('content')
        if not content:
            return Response({"detail": "Content is required"}, status=status.HTTP_400_BAD_REQUEST)

        Comment.objects.create(post=post, user=request.user, content=content)
        return Response({"detail": "Comment added"}, status=status.HTTP_201_CREATED)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('postId')
        post = Post.objects.get(id=post_id)
        serializer.save(user=self.request.user, post=post)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('postId')
        post = Post.objects.get(id=post_id)
        serializer.save(user=self.request.user, post=post)