import logging
import telegram
import datetime
from telegram.error import NetworkError, Unauthorized
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
update_id = None

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=21, minute=45)
def scheduled_job():
    bot = telegram.Bot('1083569431:AAH0uZC0dvSndasusLN_c5szzvgTKUMjEak')
    bot.send_message(chat_id='50964383', text="12:00?")

sched.start()