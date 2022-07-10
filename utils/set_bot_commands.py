import imp
from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("owner", "Pазработчик"),
        types.BotCommand("progs", "Проекты"),
        types.BotCommand("help", "Подсказка"),
        types.BotCommand("start", "Приветствие")
    ])
