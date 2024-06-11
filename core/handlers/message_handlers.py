from aiogram.types import Message

from core.database.db_commands import register_user_command, get_my_result_db, get_subject_name_db, \
    check_registration_db, create_score_db
from core.keyboards.inline import start_keyboard, get_subject_kb
from core.keyboards.reply import help_keyboard
from core.utils.machine_condition import Steps_New_Scores

from aiogram.fsm.context import FSMContext
from core.utils.schemas import ScoreValidator
from core.utils.msg import HELP_TEXT


async def user_start_bot(message: Message, ) -> None:
    await message.answer(text=f"Добрый день {message.from_user.full_name}", reply_markup=start_keyboard)


async def command_not_found(message: Message, ) -> None:
    await message.reply(text='Я вас не понял')


async def register_user(message: Message) -> None:
    user = await register_user_command(message)

    if user:
        await message.answer('Вы успешно зарегистрировались!')
    else:
        await message.answer('Вы уже зарегистрированы!')





async def view_scores(message: Message) -> None:
    result = await get_my_result_db(str(message.from_user.id))
    try:

        result_list = ''
        for x in result:
            subject = await get_subject_name_db(x.subject)
            for s in subject:
                result_list += f'{s.name} - {x.point}\n'

        await message.answer(text=result_list)
    except Exception :
        await message.answer(text='Вы ничего не добавили')


async def enter_scores(message: Message, state: FSMContext) -> None:
    if await check_registration_db(message):
        await message.answer(text='Выберите предмет', reply_markup=await get_subject_kb())
        await state.set_state(Steps_New_Scores.SELECT_SUBJECT)
    else:
        await message.answer(text='Вы не зарегистрированы')


async def write_points(message: Message, state: FSMContext) -> None:
    await state.update_data(point=message.text)

    data = await state.get_data()
    valid_data = ScoreValidator(subject=data['subject'], point=data['point'])
    await create_score_db(point=valid_data.point, subject=valid_data.subject, message=message)
    await message.answer('Запись была сохранена')
    await state.clear()


async def get_help(message: Message):
    await message.answer(text=HELP_TEXT, reply_markup=help_keyboard)
