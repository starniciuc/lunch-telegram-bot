import logging
import telegram
import datetime
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None

schedule_lanch = [
    "*Italian Lunch*\n - Supa Minestrone \n - Paste Bolognese", 
    "*Moldovan Lunch*\n - Zeama \n - Mamaliga cu tocana de pui", 
    "*Indian Lunch*\n - Supa cu somon \n - File de pui cu sos curry si orez", 
    "*American Lunch*\n - Supa crema de ciuperci \n - Costita de porc cu sos BBQ si cartofi copti", 
    "*Mexican Lunch*\n - Supa picanta de fasole \n - Fajitas de vita cu legume", 
]

don_taco_lunch_menu = [
    "*49 MDL*\n - Zeama \n - Hrisca cu tocana de pui",
    "*49 MDL*\n - Supa zilei \n - Hrisca pohodu sau paste",
    "*49 MDL*\n - Zeama \n - Hrisca cu tocana de pui",
    "*49 MDL*\n - Zeama \n - Hrisca cu tocana de pui",
    "*49 MDL*\n - Zeama \n - Hrisca cu tocana de pui",
]

def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('1083569431:AAH0uZC0dvSndasusLN_c5szzvgTKUMjEak')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
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
            # The user has removed or blocked the bot.
            update_id += 1

isSeasons = lambda text: text == 'seasons?'
isDonTaco = lambda text: text == 'dontaco?'

def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        lanch_nr_day = datetime.datetime.today().weekday()
        now = datetime.datetime.now()
        chat_id = bot.get_updates()[-1].message.chat_id
        
        if update.message:  # your bot can receive updates without messages
            global name
            global message
            if update.message.from_user:
                name = update.message.from_user.name
            # Reply to the message
            if isSeasons(update.message.text):
                message = schedule_lanch[lanch_nr_day]
                bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
            if isDonTaco(update.message.text):
                message = don_taco_lunch_menu[lanch_nr_day]
                bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
            if update.message.text == 'time?':
                message = now.strftime("%H:%M:%S")     
                bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)    
            if update.message.text == '15min':
                message = str(name) + ' bleeaaa iar!!!' 
                bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
            if update.message.text == 'coffe?':
                message = 'Jos sau la balcon?'
                bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)

if __name__ == '__main__':
    main()