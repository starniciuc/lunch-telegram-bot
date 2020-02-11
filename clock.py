import telegram

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
update_id = None

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=9, minute=30)
def scheduled_job():
    bot = telegram.Bot('1083569431:AAH0uZC0dvSndasusLN_c5szzvgTKUMjEak')
    bot.send_message(chat_id='-208886819', text="12:00?")

sched.start()