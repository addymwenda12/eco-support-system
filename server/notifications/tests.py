import responses
from django.test import TestCase
from django.conf import settings
from .sms_service import send_sms

class SMSTestCase(TestCase):
    @responses.activate
    def test_send_sms(self):
        phone_number = "+254711911416"
        message = "Test message"
        
        # Mock the Africa's Talking API response
        responses.add(
            responses.POST,
            'https://api.sandbox.africastalking.com/version1/messaging',
            json={"SMSMessageData": {"Recipients": [{"status": "Success"}]}},
            status=200
        )
        
        response = send_sms(phone_number, message)
        self.assertIsNotNone(response)
        self.assertEqual(response['SMSMessageData']['Recipients'][0]['status'], 'Success')
