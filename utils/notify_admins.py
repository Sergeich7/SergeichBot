import os
import logging

from aiogram import Dispatcher

async def on_startup_notify(dp: Dispatcher):
    for admin in os.environ.get('ADMINS').split(','):
        if admin:
            try:
                text = "Бот запущен и готов к работе"
                await dp.bot.send_message(chat_id=admin, text=text)
            except Exception as err:
                logging.exception(err)

