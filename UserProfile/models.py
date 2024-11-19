from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    display_name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to ='avatars/% y/% m/% d/')
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.username