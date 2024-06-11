from aiogram.fsm.state import State, StatesGroup


class Steps_New_Scores(StatesGroup):
    SELECT_SUBJECT = State()
    WRITE_POINTS = State()



