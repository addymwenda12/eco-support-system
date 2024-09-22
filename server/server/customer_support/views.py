from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
from .chat_service import send_message, process_message


class ChatSessionViewSet(viewsets.ModelViewSet):
  """
  A viewset for the ChatSession model.
  """
  queryset = ChatSession.objects.all()
  serializer_class = ChatSessionSerializer

  @action(detail=False, methods=['post'])
  def send_message(self, request, pk=None):
    """
    Send a message to the chat session.
    """
    session = self.get_object()
    user_message = request.data.get('message')

    if not user_message:
      return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Save user message
    ChatMessage.objects.create(session=session, sender='user', message=user_message)

    # Process message with Gemini
    bot_response = process_message(user_message)

    # Send bot response to Africa's Talking
    at_response = send_message(session.session_id, bot_response)

    if at_response:
      # Save bot response
      ChatMessage.objects.create(session=session, sender='bot', message=bot_response)
      return Response({'message': bot_response}, status=status.HTTP_200_OK)
    else:
      return Response({'error': 'Failed to send message'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  # @action(detail=False, methods=['post'])
  # def start_session(self, request):
  #   user = request.user
  #   session = ChatSession.objects.create(user=user, session_id=str(uuid.uuid4()))
  #   serializer = self.get_serializer(session)
  #   return Response(serializer.data, status=status.HTTP_201_CREATED)

  # @action(detail=True, methods=['post'])
  # def end_session(self, request, pk=None):
  #   session = self.get_object()
  #   session.end_time = timezone.now()
  #   session.save()
  #   serializer = self.get_serializer(session)
  #   return Response(serializer.data)