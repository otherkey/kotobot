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
    ["1A", "1B", "1C", "1D", "1E", "1a", "1b", "1c", "1d", "1e"],
    handle_mood
))

print("Бот запущен!")
app.run_polling()
