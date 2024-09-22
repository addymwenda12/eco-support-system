from django.contrib import admin
from .models import ChatSession, ChatMessage


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    """
    Admin interface for managing ChatSession objects.
    """
    list_display = ('user', 'session_id', 'start_time', 'end_time')
    list_filter = ('start_time', 'end_time')
    search_fields = ('user__username', 'session_id')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    """
    Admin interface for managing ChatMessage objects
    """
    list_display = ('session', 'sender', 'timestamp')
    list_filter = ('sender', 'timestamp')
    search_fields = ('session__session_id', 'message')