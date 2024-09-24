from datetime import timezone
import uuid
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer, ChatMessageSerializer
from .chat_service import send_message, process_message
from django.shortcuts import get_object_or_404


class ChatSessionViewSet(viewsets.ModelViewSet):
  """
  A viewset for the ChatSession model.
  """
  queryset = ChatSession.objects.all()
  serializer_class = ChatSessionSerializer
  lookup_field = 'session_id'
  lookup_url_kwarg = 'pk'

  def get_object(self):
    queryset = self.filter_queryset(self.get_queryset())
    lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
    assert lookup_url_kwarg in self.kwargs, (
        'Expected view %s to be called with a URL keyword argument '
        'named "%s". Fix your URL conf, or set the `.lookup_field` '
        'attribute on the view correctly.' %
        (self.__class__.__name__, lookup_url_kwarg)
    )
    filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
    obj = get_object_or_404(queryset, **filter_kwargs)
    self.check_object_permissions(self.request, obj)
    return obj

  @action(detail=True, methods=['post'])
  def send_message(self, request, pk=None):
    """
    Send a message to the chat session.
    """
    print(f"Attempting to send message for session {pk}")
    try:
      session = self.get_object()
      user_message = request.data.get('message')

      if not user_message:
        return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)

      # Save user message
      ChatMessage.objects.create(session=session, sender='user', message=user_message)

      # Process message with Gemini
      bot_response = process_message(user_message)

      # Check if the session has an associated user
      if session.user is None:
        return Response({'error': 'No user associated with this session'}, status=status.HTTP_400_BAD_REQUEST)

      # Retrieve the phone number from the user profile
      phone_number = session.user.profile.phone_number

      # Send bot response to Africa's Talking
      at_response = send_message(phone_number, bot_response)

      if at_response:
        # Save bot response
        ChatMessage.objects.create(session=session, sender='bot', message=bot_response)
        return Response({'message': bot_response}, status=status.HTTP_200_OK)
      else:
        return Response({'error': 'Failed to send message'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
      print(f"Error in send_message: {str(e)}")
      import traceback
      traceback.print_exc()
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  @action(detail=False, methods=['post'])
  def start_session(self, request):
    # user = request.user
    session = ChatSession.objects.create(session_id=str(uuid.uuid4()))
    serializer = self.get_serializer(session)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  @action(detail=True, methods=['post'])
  def end_session(self, request, pk=None):
    session = self.get_object()
    session.end_time = timezone.now()
    session.save()
    serializer = self.get_serializer(session)
    return Response(serializer.data)