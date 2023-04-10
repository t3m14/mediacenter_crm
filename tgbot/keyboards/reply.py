from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Расписание")).add(KeyboardButton(text="Тэгинг")).add(KeyboardButton(text="Настройки"))
