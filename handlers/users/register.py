
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types

from loader import dp
from states import TotalState


@dp.message_handler(Command("register"))    # /register
async def register_(message: types.Message):
    await message.answer("Привет, ты начал регистрацию,\nВведи своё имя")
    await TotalState.t1.set()


@dp.message_handler(state=TotalState.t1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(t1=answer)
    await message.answer(f"Сколько тебе лет")

    await TotalState.t2.set()


@dp.message_handler(state=TotalState.t2)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(t2=answer)

    data = await state.get_data()
    name = data.get('t1')
    years = data.get('t2')

    
    await message.answer(f"Регистрация успешно завершена\n"
                        f"твоё имя {name}\n"
                        f"тебе {years} лет")
    await state.finish()



    

