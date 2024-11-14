from django.db import models
from django.contrib.auth.models import User

class Friendship(models.Model):
    user_1 = models.ForeignKey(User, related_name='friendship_user_1', on_delete=models.CASCADE)
    user_2 = models.ForeignKey(User, related_name='friendship_user_2', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user_1', 'user_2')
    def __str__(self):
        return f"Friendship between {self.user_1.username} and {self.user_2.username}"