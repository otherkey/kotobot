import os
import random
import asyncio
from telegram import Bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, time

# 🔑 Твой токен и Chat ID
TOKEN = os.environ.get("TOKEN")
CHAT_ID = -1001492099170  # ← твой chat_id из группы

bot = Bot(token=TOKEN)

async def daily_cat():
    try:
        with open("all.jpg", "rb") as photo:
            await bot.send_photo(chat_id=CHAT_ID, photo=photo)
        print("📅 Котик по расписанию отправлен!")
    except Exception as e:
        print("Ошибка при отправке котика:", e)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("all.jpg",  "rb") as photo:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo)

async def handle_mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mood = update.message.text.lstrip("/")  # убираем слэш
    match mood:
        case "1A" | "1a":
            with open("1A.jpg",  "rb") as photo:
                await bot.send_photo(chat_id=CHAT_ID, photo=photo)
        case "1B" | "1b":
            with open("1B.jpg",  "rb") as photo:
                await bot.send_photo(chat_id=CHAT_ID, photo=photo)
        case "1C" | "1c":
            with open("1C.jpg",  "rb") as photo:
                await bot.send_photo(chat_id=CHAT_ID, photo=photo)
        case "1D" | "1d":
            with open("1D.png",  "rb") as photo:
                await bot.send_photo(chat_id=CHAT_ID, photo=photo)
        case "1E" | "1e":
            with open("1E.png",  "rb") as photo:
                await bot.send_photo(chat_id=CHAT_ID, photo=photo)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(
        ["1A", "1B", "1C", "1D", "1E", "1a", "1b", "1c", "1d", "1e"],
        handle_mood
    ))
    
    scheduler = AsyncIOScheduler()
    scheduler.add_job(daily_cat, trigger='cron', hour=13, minute=0, args=[app.bot])
    scheduler.start()
    
    print("Бот запущен!")
    await app.run_polling()

# Запуск event loop-а:
import asyncio
asyncio.run(main())
