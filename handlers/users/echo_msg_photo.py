
from random import choice

from aiogram import types

from loader import dp
from loader import bot

@dp.message_handler(content_types=["photo", "document"])
async def photo_file_id(message: types.Message):
    try:
        if message.photo[-1].file_id:
            id_photo = message.photo[-1].file_id
    except:
        id_photo = message.document.file_id
    await message.answer(
        f"ID этого файла:\n\n{id_photo}\n\nИ зачем это Вам может понадобиться?"
        )

s_no_commands_reps = [
    'Зачем вы мне это шлёте? Я все равно понимаю только команды (/help)',
    'Нет толку мне писать! Не отвечу \U0001f604 Если хотите написать создателю, то делайте это со страницы контактов (/owner)',
    'Все пишите и пишите \U0001f604 Прочтите лучше анекдот (/anek)',
    'Я не отвечаю ни на что, кроме команд (/help). Хотите анекдот (/anek)?',
    "Ваш TelegramID: {}. Может пригодится \U0001f604"
]

# отвечает на все сообщения пользователя рандомными фразами
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(
        msg.from_user.id,
        choice(s_no_commands_reps).format(str(msg.from_user.id)))


