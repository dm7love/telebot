import os
from dotenv import load_dotenv

load_dotenv()
#Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

#OpenAI ChatGPT
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#Google Calendar
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")