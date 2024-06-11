from sqlalchemy.exc import  IntegrityError

from .models import async_session, User, Subject, Result
from sqlalchemy import select, func


async def register_user_command(message):
    async with async_session() as session:
        user = User(telegram_id=str(message.from_user.id),
                    user_name=str(message.from_user.full_name)
                    )
        session.add(user)
        try:
            await session.commit()
            return True
        except IntegrityError:
            await session.rollback()
            return False


async def get_subjects_db():
    async with async_session() as session:
        return await session.scalars(select(Subject))


async def get_my_result_db(tg_id: str):
    async with async_session() as session:
        return await session.scalars(select(Result).where(User.telegram_id == tg_id).join(User).join(Subject))


async def get_subject_name_db(subject_id: int):
    async with async_session() as session:
        return await session.scalars(select(Subject).where(Subject.id == subject_id))


async def check_registration_db(message) -> bool:
    async with async_session() as session:
        connect = await session.scalars(select(User).where(User.telegram_id == str(message.from_user.id)))
        for c in connect:
            if c.id:
                return True
            return False


async def get_user_id(message) -> int:
    async with async_session() as session:
        user = await session.scalars(select(User).where(User.telegram_id == str(message.from_user.id)))
        for u in user:
            return u.id


async def create_score_db(point, subject, message):
    async with async_session() as session:
        user = await get_user_id(message)
        result = Result(point=point, subject=subject, user=user)
        session.add(result)
        try:
            await session.commit()
            return True
        except IntegrityError:
            await session.rollback()
            return False


