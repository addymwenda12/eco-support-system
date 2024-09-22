from django.db import models
from django.contrib.auth.models import User
"""
Models for the notifications app.
"""


class Notification(models.Model):
    """
    A model to store notifications for users.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a string representation of the notification.
        """
        return f"Notification for {self.user.username} at {self.sent_at}"
