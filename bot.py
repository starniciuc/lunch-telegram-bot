# Settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1083569431:AAH0uZC0dvSndasusLN_c5szzvgTKUMjEak') # Telegram API Token
dispatcher = updater.dispatcher

# Command processing
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello, do you want to talk?')
def textMessage(bot, update):
    response = 'Got youre message: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

# Handlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Here we add the handlers to the dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Start search for updates
updater.start_polling(clean=True)
# Stop the bot, if Ctrl + C were pressed
updater.idle()