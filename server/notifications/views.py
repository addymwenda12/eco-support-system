from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from .sms_service import send_sms


class NotificationViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(detail=False, methods=['post'])
    def send_notification(self, request):
        """

        """
        user = request.user
        message = request.data.get('message')
        phone_number = user.profile.phone_number

        if not message:
            return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        notification = Notification.objects.create(user=user, message=message)
        sms_response = send_sms(phone_number, message)

        if sms_response:
            notification.is_sent = True
            notification.save()
            return Response({'status': 'Notification sent successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to send notification'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
def send_test_sms(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        if not phone_number or not message:
            return JsonResponse({'error': 'Phone number and message are required'}, status=400)
        
        response = send_sms(phone_number, message)
        if response:
            return JsonResponse({'status': 'SMS sent successfully', 'response': response}, status=200)
        else:
            return JsonResponse({'error': 'Failed to send SMS'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
