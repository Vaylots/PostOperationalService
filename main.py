import os
import time
import asyncio
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()
scheduler = AsyncIOScheduler()
bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))

async def send_notification():
    chat_id = os.getenv('CHAT_ID')
    with open("schedule.jpg", "rb") as file:
        await bot.send_message(chat_id=chat_id, text="Пора закапать капли! Вот твой график:")
        await bot.send_photo(chat_id=chat_id, photo=file)
    await asyncio.sleep(10)

async def main():
    scheduler = AsyncIOScheduler()

    # 09:00
    scheduler.add_job(
        send_notification,
        "cron",
        hour=9,
        minute=0
    )

    # 13:30
    scheduler.add_job(
        send_notification,
        "cron",
        hour=13,
        minute=30
    )

    # 18:00
    scheduler.add_job(
        send_notification,
        "cron",
        hour=18,
        minute=0
    )

    # 22:30
    scheduler.add_job(
        send_notification,
        "cron",
        hour=22,
        minute=30
    )
    
    scheduler.start()

    print("Бот запущен.")
    print("Расписание: 09:00, 13:30, 18:00, 22:30")

    # Не даём программе завершиться
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())



# from apscheduler.schedulers.asyncio import AsyncIOScheduler

# scheduler = AsyncIOScheduler()

# scheduler.add_job(send_message, "cron", hour=9, minute=0)
# scheduler.add_job(send_message, "cron", hour=13, minute=30)
# scheduler.add_job(send_message, "cron", hour=18, minute=0)
# scheduler.add_job(send_message, "cron", hour=22, minute=30)

# scheduler.start()