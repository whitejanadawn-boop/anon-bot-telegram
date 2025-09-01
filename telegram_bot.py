import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your bot token from BotFather
TOKEN = "8270914861:AAGfYeNIEx15seWEFa2QKyGgFC6QpQO_fvc"

def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command."""
    update.message.reply_text("Hello! I'm your Telegram bot. Send me a text message, and I'll echo it back. Use /help for more info.")

def help_command(update: Update, context: CallbackContext) -> None:
    """Handle the /help command."""
    update.message.reply_text("Available commands:\n/start - Start the bot\n/help - Show this help message\nSend any text message to echo it back.")

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user's text message."""
    try:
        update.message.reply_text(f"You said: {update.message.text}")
    except Exception as e:
        logger.error(f"Error in echo handler: {e}")
        update.message.reply_text("Sorry, I can only process text messages.")

def error_handler(update: Update, context: CallbackContext) -> None:
    """Log errors caused by updates."""
    logger.error(f"Update {update} caused error {context.error}")

def main() -> None:
    """Run the bot."""
    try:
        # Initialize Updater with the bot token
        updater = Updater(TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        # Add handlers
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        dispatcher.add_error_handler(error_handler)

        # Start polling
        logger.info("Starting bot...")
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    main()