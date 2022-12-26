
from aiogram import types

from loader import dp
from loader import bot

from buttons.inline.do_not_click_btn import do_not_click_kb

full_text = """<b>Белашов Виталий Cергеевич</b>

\U00002705 <b><i>Хобби</i></b>
Путешествия. Последнее время ездим по стране на автомобиле.

\U00002705 <b><i>Интересы в IT</i></b>
Backend разработка. Python, SQL, Django, REST, Docker.
<a href='https://sergeich7.github.io'>Портфолио</a>
<a href='https://sergeich7.github.io/resume.pdf'>Резюме</a>
<a href='https://github.com/Sergeich7'>GitHub</a>

\U00002705 <b><i>Контакты</i></b>
@Sergeich7
pl3@yandex.ru
"""

count_progs = 0

@dp.message_handler(commands=['owner'])
@dp.message_handler(lambda message: message.text == "Контакты")
async def command_owner(message: types.Message):
    await bot.send_photo(
        message.from_user.id,
        photo='AgACAgIAAxkBAAIDq2KR95PaX7UMtL4z_mM2HsiFCWU' +
        'hAAK_ujEb7XWQSBuYVOuIeiTdAQADAgADeQADJAQ')

    global count_progs
    if not count_progs:
        # если 1ый раз вызвали программы, то выводим кнопку обманку.
        # для прикола. только 1 раз
        count_progs += 1

        await message.answer(
            full_text, parse_mode=types.ParseMode.HTML, reply_markup=do_not_click_kb,
            disable_web_page_preview=True)
    else:
        await message.answer(
            full_text, parse_mode=types.ParseMode.HTML,
            disable_web_page_preview=True)

