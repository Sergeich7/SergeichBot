
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from loader import bot
from states import TotalState


filter_kb = types.InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text='GwerwerGG',
            #    'Категория (вазы, картины ...)',
                callback_data='GGG'),
        ],
        [
            types.InlineKeyboardButton(
                'Техника (декупаж, скрапбукинг ...)',
                callback_data='gall_filter_technique')
        ],
        [
            types.InlineKeyboardButton(
                'Не использовать фильтр',
                callback_data='gall_filter_no')
        ]
    ])


@dp.message_handler(commands=['gallery'])
@dp.message_handler(lambda message: message.text == "Галерея")
async def command_gallery(message: types.Message):
    await message.answer(
        'Выберите фильтр', parse_mode=types.ParseMode.HTML,
        reply_markup=filter_kb, disable_web_page_preview=True)
    await TotalState.gall_filter_type.set()


@dp.callback_query_handler(text='GGG')
async def send_message(call: types.CallbackQuery):
    await call.answer("Кнопки заменены", show_alert=True)


@dp.message_handler(state=TotalState.gall_filter_type)
async def filter(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(gall_filter_type=answer)
    data = await state.get_data()
    await message.answer(f"{data.get('gall_filter_type')}")

#    await TotalState.t2.set()

