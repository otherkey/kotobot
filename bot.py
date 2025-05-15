import os
import random
import asyncio
from telegram import Bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Твой токен и Chat ID
TOKEN = os.environ.get("TOKEN")
CHAT_ID = -1001492099170  # ← твой chat_id из группы

bot = Bot(token=TOKEN)

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


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler(
    ["1A", "1B", "1C", "1D", "1E", "1a", "1b", "1c", "1d", "1e"],
    handle_mood
))

print("Бот запущен!")
app.run_polling()
