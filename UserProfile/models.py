from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    display_name = models.CharField(max_length=150)
    # avatar = models.ImageField(upload_to ='avatars/% y/% m/% d/',null=True,blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return {self.user} , {self.display_name}, {self.bio} 
