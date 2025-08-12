#!/usr/bin/env python3
"""
Telegram Bot that forwards any message to a specific group.
"""

import os
import logging
from typing import Union
from dotenv import load_dotenv
from telegram import Update, Message
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
TARGET_GROUP_ID = os.getenv('TARGET_GROUP_ID')
BOT_OWNER_ID = os.getenv('BOT_OWNER_ID')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required")

if not TARGET_GROUP_ID:
    raise ValueError("TARGET_GROUP_ID environment variable is required")

# Convert to int for comparison
try:
    TARGET_GROUP_ID = int(TARGET_GROUP_ID)
except ValueError:
    raise ValueError(f"Invalid TARGET_GROUP_ID: {TARGET_GROUP_ID}. It should be a valid integer (e.g., -1002716577576)")

BOT_OWNER_ID = int(BOT_OWNER_ID) if BOT_OWNER_ID else None


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Forward any message to the target group.
    """
    message = update.message
    
    # Don't forward messages from the target group itself
    if message.chat.id == TARGET_GROUP_ID:
        return
    
    # Don't forward bot commands
    if message.text and message.text.startswith('/'):
        return
    
    try:
        # Forward the message to the target group
        await message.forward(chat_id=TARGET_GROUP_ID)
        logger.info(f"Forwarded message from {message.from_user.id} to group {TARGET_GROUP_ID}")
        
        # Send confirmation to the user
        await message.reply_text("Message forwarded successfully to our support team and we will get back to you as soon as possible!")
        
    except Exception as e:
        logger.error(f"Error forwarding message: {e}")
        await message.reply_text("❌ Failed to forward message. Please try again later.")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /start command.
    """
    welcome_text = (
        "🤖 **Message Forwarding Bot**\n\n"
        "Send me any message (text, photo, video, document, etc.) and I'll forward it to the target group.\n\n"
        "✅ **Supported message types:**\n"
        "• Text messages\n"
        "• Photos and videos\n"
        "• Documents and files\n"
        "• Voice messages\n"
        "• Stickers\n"
        "• And more!\n\n"
        "Just send your message and I'll handle the rest!"
    )
    
    await update.message.reply_text(welcome_text, parse_mode='Markdown')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /help command.
    """
    help_text = (
        "📖 **Bot Commands**\n\n"
        "/start - Start the bot and see welcome message\n"
        "/help - Show this help message\n"
        "/status - Check bot status (owner only)\n\n"
        "💡 **How to use:**\n"
        "Simply send any message to this bot and it will be automatically forwarded to the target group.\n\n"
        "⚠️ **Note:** Bot commands (starting with /) are not forwarded."
    )
    
    await update.message.reply_text(help_text, parse_mode='Markdown')


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /status command (owner only).
    """
    if BOT_OWNER_ID and update.effective_user.id != BOT_OWNER_ID:
        await update.message.reply_text("❌ This command is only available to the bot owner.")
        return
    
    status_text = (
        "📊 **Bot Status**\n\n"
        f"✅ Bot is running\n"
        f"🎯 Target Group ID: `{TARGET_GROUP_ID}`\n"
        f"👤 User ID: `{update.effective_user.id}`\n"
        f"📝 Message ID: `{update.message.message_id}`\n"
        f"🕐 Timestamp: `{update.message.date}`"
    )
    
    await update.message.reply_text(status_text, parse_mode='Markdown')


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle errors.
    """
    logger.error(f"Exception while handling an update: {context.error}")


def main() -> None:
    """
    Start the bot.
    """
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(MessageHandler(filters.COMMAND & filters.Regex("^/start$"), start_command))
    application.add_handler(MessageHandler(filters.COMMAND & filters.Regex("^/help$"), help_command))
    application.add_handler(MessageHandler(filters.COMMAND & filters.Regex("^/status$"), status_command))
    
    # Add message handler for all other messages (forward them)
    application.add_handler(MessageHandler(filters.ALL, forward_message))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main() 