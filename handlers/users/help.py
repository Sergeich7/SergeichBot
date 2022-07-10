from aiogram import types

from loader import dp

full_text = """<b>Команды бота</b>

/anek Анекдот
/help Подсказка
/owner Информация о разработчике
/progs Примеры программ
/start Приветствие
"""

@dp.message_handler(commands=["help"])
async def commands_help(message: types.Message):
    await message.answer(
            full_text,
            parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
