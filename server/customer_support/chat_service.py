import africastalking
import google.generativeai as genai
from django.conf import settings
# from africastalking.SMS import SMS


# Initialize AfricasTalking
africastalking.initialize(
    username=settings.AFRICASTALKING_USERNAME,
    api_key=settings.AFRICASTALKING_API_KEY
)
sms = africastalking.SMS

# Initialize Google Generative AI
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def send_message(phone_number, message):
  """
  Send message to Africa's Talking Chat API
  """
  try:
    response = sms.send(message, [phone_number])
    return response
  except Exception as e:
    print(f"Error sending message: {e}")
    return None

def process_message(message):
  """
  Use Gemini to generate a response
  """
  try:
    response = model.generate_content(message)
    return response.text
  except Exception as e:
    print(f"Error processing message with Gemini: {e}")
    return "I'm sorry, I'm having trouble processing your message."

