from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta    


scheduler = BackgroundScheduler()


def my_cron_job():
    print(f"Running job at {datetime.utcnow()}")

def start_scheduler():
    scheduler.add_job(
        my_cron_job,
        trigger="cron",
        minute="*/1"   # runs every 1 minute
    )
    scheduler.start()