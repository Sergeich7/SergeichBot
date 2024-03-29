"""

Бот @bvsSergeichBot. Разработан в демонстрационных целях

Использованы библиотеки:
aiogram

Последние изменение: 09.08.2022

"""

import os
from aiogram.utils import executor

############################################
# Переменные окружения
if not os.environ.get('TOKEN'):
    # Запуск сервера без докера (разработка или на виртуале)
    # Нет переменных окружения. Загружаем из файла.
    from dotenv import load_dotenv
    if os.path.exists('.env'):
        load_dotenv('.env')

from handlers import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)
    print("Бот запущен")

if __name__ == "__main__":

    executor.start_polling(dp, on_startup=on_startup)
