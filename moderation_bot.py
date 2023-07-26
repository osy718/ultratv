import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with the token obtained from BotFather
bot_token = '6089411781:AAFbwfXMpdVxxlq2fJFnbkLEQW7kqM8V1_o'

# Create the Updater and pass the bot token to it
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your group moderation bot.')

# Command to kick users
def kick_user(update: Update, context: CallbackContext) -> None:
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        context.bot.kick_chat_member(update.message.chat_id, user_id)
        update.message.reply_text(f'User {user_id} has been kicked.')
    else:
        update.message.reply_text('Please use this command as a reply to the message of the user you want to kick.')

# Command to ban users
def ban_user(update: Update, context: CallbackContext) -> None:
    if update.message.reply_to_message:
        user_id = update.message.reply_to_message.from_user.id
        context.bot.ban_chat_member(update.message.chat_id, user_id)
        update.message.reply_text(f'User {user_id} has been banned.')
    else:
        update.message.reply_text('Please use this command as a reply to the message of the user you want to ban.')

# Command to unban users
def unban_user(update: Update, context: CallbackContext) -> None:
    if context.args:
        user_id = int(context.args[0])
        context.bot.unban_chat_member(update.message.chat_id, user_id)
        update.message.reply_text(f'User {user_id} has been unbanned.')
    else:
        update.message.reply_text('Please provide the user ID you want to unban.')

# Message handler to respond to user messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('I can only process commands like /kick, /ban, and /unban.')

# Set up the command and message handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('kick', kick_user))
dispatcher.add_handler(CommandHandler('ban', ban_user))
dispatcher.add_handler(CommandHandler('unban', unban_user))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the bot
updater.start_polling()
updater.idle()
