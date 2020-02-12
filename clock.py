import telegram
import os
from apscheduler.schedulers.blocking import BlockingScheduler
TOKEN = os.environ.get('TOKEN', "")
sched = BlockingScheduler()
update_id = None

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=9, minute=30)
def scheduled_job():
    bot = telegram.Bot(TOKEN)
    bot.send_message(chat_id='-208886819', text="12:00?")

@sched.scheduled_job('cron', day_of_week='fri', hour=14, minute=00)
def scheduled_job():
    bot = telegram.Bot(TOKEN)
    bot.send_message(chat_id='-208886819', text="Azzziii e vineeereaa!!!! https://www.youtube.com/watch?v=TAJ4WHNFwck")

sched.start()