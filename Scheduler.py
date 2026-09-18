from apscheduler.schedulers.asyncio import AsyncIOScheduler
class Scheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    def add_job(self, func:callable, hour:int, minute:int):
        self.scheduler.add_job(func, "cron", hour=hour, minute=minute)
        
    def add_jobs(self, func:callable, times:list):
        for time in times:
            self.scheduler.add_job(func, "cron", hour=time["hour"], minute=time["minute"])
        
    def start(self):
        self.scheduler.start()