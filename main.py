import os
import time
import asyncio
from dotenv import load_dotenv
from telegram import Bot
from Scheduler import Scheduler
load_dotenv()
scheduler = Scheduler()
bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))

async def send_notification():
    chat_id = os.getenv('CHAT_ID')
    with open("schedule.jpg", "rb") as file:
        await bot.send_message(chat_id=chat_id, text="Пора закапать капли! Вот твой график:")
        await bot.send_photo(chat_id=chat_id, photo=file)
    await asyncio.sleep(10)
    
async def check_schedule() -> None:
    
    pass
   
async def main() -> None:
    times = [
        {"hour": 9, "minute": 0},
        {"hour": 13, "minute": 30},
        {"hour": 18, "minute": 0},
        {"hour": 22, "minute": 30},
    ]
    scheduler.add_jobs(send_notification, times)
    
    scheduler.start()

    print("Бот запущен.")
    print("Расписание: 09:00, 13:30, 18:00, 22:30")

    # Не даём программе завершиться
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())



