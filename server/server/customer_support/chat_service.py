import africastalking
import google.generativeai as genai
from django.conf import settings


# Initialize AfricasTalking
africastalking.initialize(
  username=settings.AFRICASTALKING_USERNAME,
  api_key=settings.AFRICASTALKING_API_KEY
)
chat = africastalking.Chat

# Initialize Google Generative AI
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def send_message(session_id, message):
  """
  Send message to Africa's Talking Chat API
  """
  try:
    response = chat.send(session_id, message)
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

