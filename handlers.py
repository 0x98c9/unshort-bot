import time
from collections import defaultdict, deque
from telegram import Update
from telegram.ext import ContextTypes
from config import RATE_LIMIT
from logger import logger
from unshortener import unshorten_url

# Rate limiting storage
user_requests = defaultdict(deque)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message"""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! Send me any shortened URL (e.g., bit.ly) "
        "and I'll reveal the original link."
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the user starts the bot."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! Send me a shortened URL, and I'll reveal the original link."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message."""
    await update.message.reply_text(
        "📌 *How to Use:*\n\n"
        "1️⃣ Send me any shortened link (e.g., bit.ly, tinyurl, etc.)\n"
        "2️⃣ I will return the original long link.\n\n"
        "⚠️ *Rate Limit:* 5 requests per minute per user."
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send an about message."""
    await update.message.reply_text(
        "🤖 *Link Unshortener Bot*\n\n"
        "Developed with ❤️ using Python & httpx.\n"
        "This bot helps you reveal the original URL behind shortened links."
    )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle unknown commands."""
    await update.message.reply_text("❌ Sorry, I didn't understand that command.")

def check_rate_limit(user_id: int) -> bool:
    """Enforce rate limiting"""
    now = time.time()
    window = 60  # 1 minute
    
    while user_requests[user_id] and user_requests[user_id][0] < now - window:
        user_requests[user_id].popleft()
    
    if len(user_requests[user_id]) >= RATE_LIMIT:
        return True
    
    user_requests[user_id].append(now)
    return False

async def process_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle URL unshortening"""
    user = update.effective_user
    url = update.message.text.strip()

    if check_rate_limit(user.id):
        await update.message.reply_text("⚠️ Rate limit exceeded (5 requests/minute). Please wait.")
        return
    
    if not url.startswith(("http://", "https://")):
        await update.message.reply_text("❌ Invalid URL format. Please include http:// or https://")
        return
    
    result = await unshorten_url(url)
    await update.message.reply_text(f"🔗 Original URL:\n{result}")
