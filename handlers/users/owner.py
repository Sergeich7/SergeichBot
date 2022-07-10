
from aiogram import types

from loader import dp
from loader import bot

from buttons.inline.do_not_click_btn import do_not_click_kb

full_text = """<b>Белашов Виталий Cергеевич</b>

\U00002705 <b><i>Область интересов</i></b>
Создание парсеров, ботов для телеграмм и любых других программ.

\U00002705 <b><i>Основные навыки</i></b>
Для разработки я использую Python, SQL, NumPy, Pandas.

<a href='https://docs.google.com/document/d/1lJz-qQMQEXvIPcA_HFfSTSj9MsxpI-RrbJXlKFhkzzg/edit?usp=sharing'>Резюме</a>

https://t.me/Sergeich7
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

