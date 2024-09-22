import africastalking
from django.conf import settings
"""
Service for sending SMS notifications.
"""


# Initialize the AfricasTalking SDK
africastalking.initialize(
    username=settings.AFRICAS_TALKING_USERNAME,
    api_key=settings.AFRICAS_TALKING_API_KEY
)

sms = africastalking.SMS

def send_sms(phone_number, message):
    """
    Send an SMS to the specified phone number.
    """
    try:
        response = sms.send(message, [phone_number])
        print(response)
        return response
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return None
