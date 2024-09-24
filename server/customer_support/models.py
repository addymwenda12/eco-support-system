from django.db import models
from django.contrib.auth.models import User
"""
Module to store chat sessions and messages.
"""


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
