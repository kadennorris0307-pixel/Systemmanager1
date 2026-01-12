from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def fetch_and_analyze():
    print("Auto analysis running")

def start_scheduler():
    scheduler.add_job(fetch_and_analyze, "interval", minutes=5, id="auto")
    scheduler.start()
