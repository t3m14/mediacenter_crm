from aiogram import Dispatcher
from aiogram.types import Message
from ..keyboards.reply import *

async def user_start(message: Message):
    await message.reply(f"Привет, {message.from_user.first_name}!\nВыбери то что тебе нужно в меню ниже", reply_markup=main_menu)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
