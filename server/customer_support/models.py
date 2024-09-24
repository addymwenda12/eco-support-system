from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
"""
Module to store chat sessions and messages.
"""


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

class ChatSession(models.Model):
  """
  A model to store chat sessions.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  session_id = models.CharField(max_length=100, unique=True)
  start_time = models.DateTimeField(auto_now_add=True)
  end_time = models.DateTimeField(null=True, blank=True)

class ChatMessage(models.Model):
  """
  A model to store chat messages.
  """
  session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
  sender = models.CharField(max_length=100)
  message = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
