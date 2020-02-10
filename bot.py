import logging
import telegram
import datetime
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None

schedule_lanch = [
    "*Italian Lunch*\n - Supa Minestrone \n - Paste Bolognese", 
    "*Moldovan Luuch*\n - Zeama \n - Mamaliga cu tocana de pui", 
    "*Indian Lunch*\n - Supa cu somon \n - File de pui cu sos curry si orez", 
    "*American Lunch*\n - Supa crema de ciuperci \n - Costita de porc cu sos BBQ si cartofi copti", 
    "*Mexican Lunch*\n - Supa picanta de fasole \n - Fajitas de vita cu legume", 
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


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        lanch_nr_day = datetime.datetime.today().weekday()
        now = datetime.datetime.now()
        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            if update.message.text == 'sesson?':
                update.message.reply_text(schedule_lanch[lanch_nr_day], parse_mode=telegram.ParseMode.MARKDOWN)
            if update.message.text == 'time?':
                update.message.reply_text(now.strftime("%H:%M:%S"))

if __name__ == '__main__':
    main()