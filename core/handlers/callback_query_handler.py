from aiogram.types import Message, CallbackQuery

from core.handlers.message_handlers import register_user
from core.utils.machine_condition import Steps_New_Scores

from aiogram.fsm.context import FSMContext


async def register_kb_callback(callback: CallbackQuery):
    if callback.data == 'register':
        await register_user(callback.message)



async def subject_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Steps_New_Scores.WRITE_POINTS)
    await state.update_data(subject=callback.data.split("_")[1])
    return await callback.message.answer(text=f'Введите баллы')


