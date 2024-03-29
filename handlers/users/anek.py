
import sqlite3

from aiogram import types

from loader import dp

sql_create_anek = """
create table anek(txt text);
insert into
    anek (txt)
values
    ('\U0001F4A5 Если у 5 человек рядом с вами такие же сапоги - это не мода. Это армия.'),
    ('\U0001F608 Себя не обманешь, но попытки продолжаются.'),
    ('\U0001F6BD Недавно прочитал слово унитаз наоборот, теперь боюсь на него сесть.'),
    ('\U00002668 Купила успокоительный чай, а меня бесит его запах и вкус.'),
    ('\U0001F3E6 Успешная международная корпорация ищет менеджера со своей клиентской базой.'),
    ('\U0001F494 Ненавижу тебя настолько, что печатаю тебе это только средним пальцем.'),
    ('\U0001F4F1 Отсутствие айфона - высшая форма аскетизма.'),
    ('\U0001F4F1 Розыгрыш бесплатного айфона оказался розыгрышем.'),
    ('\U0001F620 Не надо все понимать. Люди, которые все понимают, целыми днями злятся.'),
    ('\U0001F9A5 Мы просыпаемся вместе. Я и моя лень.'),
    ('\U0001F482 Плох тот генерал, который не перестал быть солдафоном.'),
    ('\U0001F37A Если ты пьяный, то это еще не повод не выпить.'),
    ('\U0001F6CB Если не можешь усидеть на двух стульях, приляг на диванчик.'),
    ('\U0001F6CC Смирись с неизбежным. Тебе не выспаться.'),
    ('\U0001F525 От зависти не умирают, от зависти убивают.'),
    ('\U0001F442 Ван Гог не обращал внимания на критику, точнее слушал ее вполуха.'),
    ('\U0001F92F Голова легкой должна быть. Чем меньше знаний, тем крепче убеждения.'),
    ('- Изя, ты оказался не тем, чем я думала...\n- Сара, а чем ты таки думала?\n\U0001F970'),
    ('\U0001F64A Все, что не делается, я и не делаю.'),
    ('\U0001F9D0 Самый лучший понедельник - это тот, который выходной.'),
    ('\U0001F354 Полезное от приятного отличается отвратительным вкусом.');
"""

sql_random_anek = 'select txt from anek order by random() limit 1;'

@dp.message_handler(commands=['anek'])
@dp.message_handler(lambda message: message.text == "Анекдот")
async def command_anek(message: types.Message):

    sb_con = sqlite3.connect("SergeichBot.db")
    sb_cur = sb_con.cursor()

    while True:
        try:
            sb_cur.execute(sql_random_anek)
            break
        except sqlite3.DatabaseError as err:
            if 'no such table: anek' in str(err):
                try:
                    sb_cur.executescript(sql_create_anek)
                except sqlite3.DatabaseError as err:
                    print("Ошибка", err)
            else:
                print("Ошибка", err)

    await message.answer(sb_cur.fetchone()[0],
            parse_mode=types.ParseMode.MARKDOWN, disable_web_page_preview=True)

    sb_cur.close()
    sb_con.close()
