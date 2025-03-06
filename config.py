import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get bot token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("⚠️ TELEGRAM_BOT_TOKEN is not set in the .env file!")
# Rate Limiting
RATE_LIMIT = 5  # Requests per minute per user
REQUEST_TIMEOUT = 10  # Timeout for HTTP requests
