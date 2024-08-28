from fastapi import FastAPI, HTTPException
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.utils import executor
from tortoise import Tortoise
from tortoise.models import Model
from tortoise.fields import CharField
from pydantic import BaseModel
import os
import uuid

# Initialize FastAPI app
app = FastAPI()

# Initialize Telegram bot
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Define the User model
class User(Model):
    id = CharField(max_length=50, primary_key=True)
    username = CharField(max_length=50)

    class Meta:
        table = "user"

@app.on_event("startup")
async def startup():
    await Tortoise.init(
        db_url=os.getenv("DATABASE_URL"),
        modules={"models": ["main"]}
    )
    await Tortoise.generate_schemas()

@app.on_event("shutdown")
async def shutdown():
    await Tortoise.close_connections()

# Handle Telegram bot commands
@dp.message_handler(commands=['start'])
async def send_welcome(message):
    await message.reply("Welcome!")

@app.post("/webhook")
async def webhook(update: Update):
    await dp.process_update(update)
    return {"status": "ok"}

# Define Pydantic model for user creation
class UserIn(BaseModel):
    username: str

@app.post("/api/users/")
async def create_user(user_in: UserIn):
    user = await User.create(id=str(uuid.uuid4()), username=user_in.username)
    return {"id": user.id, "username": user.username}

@app.get("/api/users/{user_id}")
async def get_user(user_id: str):
    user = await User.filter(id=user_id).first()
    if user:
        return {"id": user.id, "username": user.username}
    raise HTTPException(status_code=404, detail="User not found")
