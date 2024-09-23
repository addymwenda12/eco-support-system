from rest_framework import serializers
from .models import ChatSession, ChatMessage


class ChatSessionSerializer(serializers.ModelSerializer):
  """
  A serializer for the ChatSession model.
  """
  class Meta:
    model = ChatSession
    fields = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
  """
  A serializer for the ChatMessage model.
  """
  class Meta:
    model = ChatMessage
    fields = '__all__'
