from aiogram import types

from buttons.keyboard.keyboard_menu import kb_menu

#from total_btn import kb_menu

from loader import dp
from handlers.users.programms import full_text as p_full_text
from handlers.users.help import full_text as h_full_text

full_text = """

Я бот <b>Сергеич</b>! Моя главная задача - прославлять гений создателя (/owner)! ШУТКА! \U0001f604 Хотя...

Вы можете мне что нибудь написать или отправить фотку.

Так же есть возможность ознакомиться с разработанными программами (/progs). Они отлично демонстрируют возможности и стиль программирования.

""" + h_full_text

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):

    await message.answer(
            f"Привет {message.from_user.full_name}!" + full_text, reply_markup=kb_menu,
            parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)


