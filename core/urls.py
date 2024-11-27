from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.contrib import admin
from django.urls import path, include
from Post.views import ( PostListCreateAPIView, PostLikeAPIView, PostCommentAPIView, CommentListCreateAPIView, LikeListCreateAPIView )
from .views import UserView
from django.conf import settings
from django.conf.urls.static import static
from Post.views import GetPostSerializer
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/users/', UserView.as_view(), name='user-list'),
    path('api/posts', PostListCreateAPIView.as_view(), name='post-detail'),
    path('api/posts/<int:pk>/comment', PostCommentAPIView.as_view()),
    path('api/posts/<int:pk>/like', PostLikeAPIView.as_view()),
    path('api/like', LikeListCreateAPIView.as_view()),
    path('api/comment', CommentListCreateAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
