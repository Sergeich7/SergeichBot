
from aiogram import types

from loader import dp

full_text = """
<b>Программы</b>

Здесь только самые интересные проекты. Иходный код и другие программы Вы найдете на <a href='https://github.com/Sergeich7'>GitHub</a>

\U00002705 <b><i>ПАРСЕРЫ</i></b>

<b><i>yandex2gis</i></b> - в многопоточном режиме получает с сайтов 2gis.ru и yandex.ru/maps названия боулингов Москвы и ссылки на карточки. Программа написана на Python (selenium и beautifulsoup) c использованием ООП.

<b><i>ЛесХоз</i></b> - с сайта lesegais.ru программа выкачивает всю информацию по сделкам с древесиной. Пришлось запустить 2 потока на встречу друг другу. И все равно парсинг длится ~19 часов (~220000 сделок).

\U00002705 <b><i>SQL-Database</i></b>

<b><i>Ять</i></b> - база данных ресторана разработана на СУБД PostgreSQL в рамках аттестационной работы курса "Базы данных. SQL" РАНХиГС.

\U00002705 <b><i>ТЕЛЕГРАМ БОТ</i></b>

<b><i>Бот Сергеич</i></b> - Да! Да! \U0001f604 Этот самый бот. Разработан в демонстрационных целях.

\U00002705 <b><i>САЙТ</i></b>

<b><i><a href="https://artgallery-tatyana.ru/">Арт-галерея "Татьяна"</a></i></b> - Выставка декоративного искусства. Здесь собраны лучшие работы друзей и единомышленников.


"""

@dp.message_handler(commands=["progs"])
@dp.message_handler(lambda message: message.text == "Программы")
async def command_programms(message: types.Message):
    await message.answer(
        full_text, parse_mode=types.ParseMode.HTML,
        disable_web_page_preview=False)
