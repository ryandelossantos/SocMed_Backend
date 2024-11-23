from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from django.contrib import admin
from django.urls import path
from UserProfile.views import UserProfileView
from Post.views import PostView , AddCommentView
from .views import UserView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/users/' , UserView.as_view()),
    path('api/profiles/' , UserProfileView.as_view()),
    path('api/posts/' , PostView.as_view()),
    path('api/addcomment/' , AddCommentView.as_view()),
]
