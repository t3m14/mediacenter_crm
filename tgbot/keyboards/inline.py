from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

settings_menu = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Чаты", callback_data="chats")
                                           ).add(InlineKeyboardButton(text="Рассылка", callback_data="sending"))
