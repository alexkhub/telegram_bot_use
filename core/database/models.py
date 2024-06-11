from datetime import datetime
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs

from sqlalchemy.orm import DeclarativeBase
from core.config import DB_LINK

engine = create_async_engine(f"sqlite+aiosqlite:///{DB_LINK}\\bot_db.sqlite3")

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, )
    user_name = Column(String(50), nullable=False)
    telegram_id = Column(String(70), unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.now())


class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True, )
    name = Column(String(50), unique=True, nullable=False)


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True, )
    subject = Column(Integer, ForeignKey('subject.id'))
    user = Column(Integer, ForeignKey('user.id'))
    point = Column(Integer)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
