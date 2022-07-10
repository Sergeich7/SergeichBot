from aiogram import types

from loader import dp
from loader import bot

# обработчик событий кнопок
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_do_not_click(callback_query: types.CallbackQuery):
    if callback_query.data[3:] == '_do_not_click':
        await bot.answer_callback_query(
            callback_query.id, text='ЭXX 😉 НЕ КЛИКАЙТЕ СЮДА БОЛЬШЕ❗',
            show_alert=True)
