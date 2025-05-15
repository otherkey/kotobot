import os
import random
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# 🔑 Твой токен и Chat ID
TOKEN = os.environ.get("TOKEN")
CHAT_ID = -1001492099170  # ← твой chat_id из группы

bot = Bot(token=TOKEN)

#  По расписанию
async def daily_cat():
    try:
        with open("all.jpg", "rb") as photo:
            await bot.send_photo(chat_id=CHAT_ID, photo=photo)
        print("📅 Котик по расписанию отправлен!")
    except Exception as e:
        print("Ошибка при отправке котика:", e)

#  /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("all.jpg",  "rb") as photo:
        await update.message.reply_photo(photo)

#  /1A... /1E
async def handle_mood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mood = update.message.text.lstrip("/")  # убираем слэш
    match mood:
        case "1A" | "1a":
            filename = "1A.jpg"
        case "1B" | "1b":
            filename = "1B.jpg"
        case "1C" | "1c":
            filename = "1C.jpg"
        case "1D" | "1d":
            filename = "1D.png"
        case "1E" | "1e":
            filename = "1E.png"
        case "1F" | "1f":
            filename = "1F.png"
        case "2A" | "2a":
            filename = "2A.jpg"
        case "2B" | "2b":
            filename = "2B.png"
        case "2C" | "2c":
            filename = "2С.png"
        case "2D" | "2d":
            filename = "2D.jpg"
        case "2E" | "2e":
            filename = "2E.png"
        case "2F" | "2f":
            filename = "2F.png"
        case "3A" | "3a":
            filename = "3A.png"
        case "3B" | "3b":
            filename = "3B.png"
        case "3C" | "3c":
            filename = "3C.png"
        case "3D" | "3d":
            filename = "3D.png"
        case "3E" | "3e":
            filename = "3E.png"
        case "3F" | "3f":
            filename = "3F.png"
        case "4A" | "4a":
            filename = "4A.png"
        case "4B" | "4b":
            filename = "4B.png"
        case "4C" | "4c":
            filename = "4C.png"
        case "4D" | "4d":
            filename = "4D.png"
        case "4E" | "4e":
            filename = "4E.png"
        case "4F" | "4f":
            filename = "4F.png"
        case "5A" | "5a":
            filename = "5A.png"
        case "5B" | "5b":
            filename = "5B.png"
        case "5C" | "5c":
            filename = "5C.png"
        case "5D" | "5d":
            filename = "5D.png"
        case "5E" | "5e":
            filename = "5E.png"
        case "5F" | "5f":
            filename = "5F.png"
        case "6A" | "6a":
            filename = "6A.png"
        case "6B" | "6b":
            filename = "6B.png"
        case "6C" | "6c":
            filename = "6C.png"
        case "6D" | "6d":
            filename = "6D.png"
        case "6E" | "6e":
            filename = "6E.png"
        case "6F" | "6f":
            filename = "6F.png"
        case _:
            return  # ничего не делать

    with open(filename, "rb") as photo:
        await update.message.reply_photo(photo)
        

# 🧠 Настройка бота
scheduler = AsyncIOScheduler()

async def start_scheduler(app: object) -> None:
    scheduler.add_job(daily_cat, trigger="cron", hour=13, minute=0)
    scheduler.start()
    print("⏰ Планировщик запущен")

app = ApplicationBuilder().token(TOKEN).post_init(start_scheduler).build()

# Команды
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler(
    ["1A", "1B", "1C", "1D", "1E", "1a", "1b", "1c", "1d", "1e", "1F", "1f", "2A", "2B", "2D", "2E", "2F", "2C", "3A", "3B", "3C", "3D", "3E", "3F", "4A", "4B", "4C", "4D", "4E", "4F", "5A", "5B", "5C", "5D", "5E", "5F", "6A", "6B", "6C", "6D", "6E", "6F", "2a", "2b", "2c", "2d", "2e", "2f", "3a", "3b", "3c", "3d", "3e", "3f", "4a", "4b", "4c", "4d", "4e", "4f", "5a", "5b", "5c", "5d", "5e", "5f", "6a", "6b", "6c", "6d", "6e", "6f"],
    handle_mood
))

print("Бот запущен!")
app.run_polling()
