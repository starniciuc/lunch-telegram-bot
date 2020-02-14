import logging
import telegram
import datetime
import os
import json
from telegram.error import NetworkError, Unauthorized
from time import sleep

TOKEN = os.environ.get('TOKEN', "")
PORT = int(os.environ.get('PORT', '8443'))
#updater = Updater(TOKEN)
# add handlers
#updater.start_webhook(listen="0.0.0.0",
#                      port=PORT,
#                      url_path=TOKEN)
#updater.bot.set_webhook("https://lanchtime-bot.herokuapp.com/" + TOKEN)
#updater.idle()

update_id = None
data = {}

def main():
    global update_id
    global data
    bot = telegram.Bot(TOKEN)
    with open('data.json') as json_file:
        data = json.load(json_file)
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1

def echo(bot):
    global update_id
    global data
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        lunch_nr_day = datetime.datetime.today().weekday()
        now = datetime.datetime.now()
        chat_id = bot.get_updates()[-1].message.chat_id
        
        if update.message:
            name = ''
            message = ''
            if update.message.from_user:
                name = update.message.from_user.name
            try:
                if data[update.message.text]:
                    message = data[update.message.text][lunch_nr_day]
            except:
                print(data)
                message = 'Not found'    
            if update.message.text == '15min':
                message = str(name) + ' bleeaaa iar!!!' 
            if update.message.text == 'coffe?':
                message = 'Jos sau la balcon?'
            bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
    
if __name__ == '__main__':
    main()