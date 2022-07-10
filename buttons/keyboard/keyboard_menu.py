

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_menu.row(
    KeyboardButton(text='Контакты', callback_data='btn_owner'),
    KeyboardButton( text='Программы', callback_data='btn_progs'),
    KeyboardButton( text='Анекдот', callback_data='btn_anek')
    )
