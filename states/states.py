
from aiogram.dispatcher.filters.state import State, StatesGroup


class TotalState(StatesGroup):

    gall_filter_type = State()
    gall_filter_num = State()

    click_on_inline = State()
    teleg_id = State()
    teleg_name = State()
    last_enter_date = State()

    name = State()
    t1 = State()
    t2 = State()
