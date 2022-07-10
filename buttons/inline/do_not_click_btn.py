

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

do_not_click_btn = InlineKeyboardButton(
            'Не кликайте сюда ☠️', callback_data='btn_do_not_click')

do_not_click_kb = InlineKeyboardMarkup().add(do_not_click_btn)
