from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram_calendar import simple_cal_callback, SimpleCalendar
from ..keyboards.inline import *
async def handle_reply(message: Message):
    if message.text == "Рассылка":
        await message.answer("Вы в меню рассылки")
    if message.text == "Настройки":
        await message.answer("Вы в меню настройки", reply_markup=settings_menu)
    if message.text == "Тэгинг":
        await message.answer("Вы в меню тэгинга")
        await message.answer("Выберете дату", reply_markup=await SimpleCalendar().start_calendar())

# Работа с календарём
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'Выбран день {date.strftime("%d/%m/%Y")}'
        )
def register_reply(dp: Dispatcher):
    dp.register_message_handler(handle_reply, handle_reply, state="*")
    dp.register_callback_query_handler(process_simple_calendar, simple_cal_callback.filter())
