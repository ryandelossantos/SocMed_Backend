from django.contrib import admin
from .models import Message,Conversation,ConversationParticipant
admin.site.register(Message)
admin.site.register(Conversation)
admin.site.register(ConversationParticipant)