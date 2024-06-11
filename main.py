import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher, F
from aiogram.filters import  Command
from core.config import TOKEN
from core.handlers.message_handlers import *
from core.handlers.callback_query_handler import *
from core.utils.machine_condition import Steps_New_Scores
from core.database.models import async_main
dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, )
    # await async_main() # создание БД
    dp.message.register(user_start_bot, Command(commands=['start']))
    dp.message.register(register_user, Command(commands=['register']))
    dp.message.register(view_scores, Command(commands=['view_scores']))
    dp.message.register(enter_scores, Command(commands=['enter_scores']))
    dp.message.register(get_help, Command(commands=['help']))
    dp.callback_query.register(subject_callback, Steps_New_Scores.SELECT_SUBJECT )
    dp.message.register(write_points, Steps_New_Scores.WRITE_POINTS)


    dp.callback_query.register(register_kb_callback)
    dp.message.register(command_not_found)

    await dp.start_polling(bot)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
