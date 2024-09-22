from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'sent_at', 'is_sent')
    list_filter = ('is_sent', 'sent_at')
    search_fields = ('user__username', 'message')

