from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN
from logger import logger
from handlers import start, process_url, help_command, about, unknown

def main():
    """Start the bot"""
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_url))

    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
