from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_group = models.BooleanField(default=False)

    def __str__(self):
        return f"Group Conversation: {self.is_group} on {self.created_at}"

class ConversationParticipant(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='participants')
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('conversation', 'user_profile')

    def __str__(self):
        return f"{self.user_profile.username} in {self.conversation.id}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} in {self.conversation.id} at {self.timestamp}"
