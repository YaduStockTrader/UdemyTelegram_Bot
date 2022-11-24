# This is a sample Python script.
from telegram.ext import (Updater, CommandHandler)
import os
TOKEN=os.getenv("UDEMY_BOT_TOKEN")
# Press the green button in the gutter to run the script.

def start_handler(update,context):
    update.message.reply_text(f"Hello Creator! ")
if __name__ == '__main__':
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN,use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    dispatcher.add_handler(CommandHandler("start", start_handler))

    # Start the Bot
    updater.start_polling()
