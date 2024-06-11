from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.database.db_commands import get_subjects_db
from aiogram.utils.keyboard import InlineKeyboardBuilder
start_keyboard = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='register',
                callback_data='register'

            ),

        ]
    ]
)


async def get_subject_kb():
    subjects = await get_subjects_db()

    subject_list_keyboard = InlineKeyboardBuilder()

    for subject in subjects:

        subject_list_keyboard.add(InlineKeyboardButton(text=subject.name, callback_data=f'subject_{subject.id}'))
    return subject_list_keyboard.adjust(2).as_markup()
