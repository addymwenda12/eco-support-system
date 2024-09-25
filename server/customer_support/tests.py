import responses
from django.test import TestCase
from django.conf import settings
from .chat_service import send_message, process_message

class ChatServiceTestCase(TestCase):
    @responses.activate
    def test_send_message(self):
        phone_number = "+254711911416"
        message = "Test message"
        
        # Mock the Africa's Talking API response
        responses.add(
            responses.POST,
            'https://api.sandbox.africastalking.com/version1/messaging',
            json={"SMSMessageData": {"Recipients": [{"status": "Success"}]}},
            status=200
        )
        
        response = send_message(phone_number, message)
        self.assertIsNotNone(response)
        self.assertEqual(response['SMSMessageData']['Recipients'][0]['status'], 'Success')

    @responses.activate
    def test_process_message(self):
        message = "Hello, how can I help you?"
        
        # Mock the Google Generative AI response
        responses.add(
            responses.POST,
            'https://api.generativeai.com/v1/models/gemini-1.5-flash-latest:generateContent',
            json={"text": "Hello! How can I assist you today?"},
            status=200
        )
        
        response = process_message(message)
        self.assertEqual(response, "Hello! How can I assist you today?")