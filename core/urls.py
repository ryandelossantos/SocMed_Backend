from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.contrib import admin
from django.urls import path, include
from UserProfile.views import UserProfileView
from Post.views import PostViewSet, CommentViewSet, LikeViewSet
from .views import UserView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/users/', UserView.as_view(), name='user-list'),
    path('api/profiles/', UserProfileView.as_view()),
    path('api/posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/posts/<int:postId>/addcomment/', CommentViewSet.as_view({'post': 'create'})),
    path('api/posts/<int:postId>/like/', LikeViewSet.as_view({'post': 'create'})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
