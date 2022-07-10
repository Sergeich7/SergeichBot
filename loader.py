
from aiogram import Bot, types, Dispatcher

import config

bot = Bot(config.TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

