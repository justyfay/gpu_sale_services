from __future__ import annotations

from sqlalchemy import CTE, MetaData, Select
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.compiler import SQLCompiler
from sqlalchemy.sql.dml import ReturningInsert, ReturningUpdate

from src.ms_sender.config import settings
from src.ms_sender.logger import get_logger

logger = get_logger()

engine: AsyncEngine = create_async_engine(url=settings.database_url)
async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base(metadata=MetaData(schema="sender"))


class SessionContextManager:
    def __init__(self) -> None:
        self.session_factory = async_session_maker
        self.session = None

    async def __aenter__(self) -> SessionContextManager:
        logger.debug("Enter in context.")
        self.session = self.session_factory()
        return self

    async def __aexit__(self, *args: object) -> None:
        logger.debug("Exit from context.")
        await self.rollback()

    async def commit(self) -> None:
        await self.session.commit()
        await self.session.close()

    async def rollback(self) -> None:
        await self.session.rollback()
        await self.session.close()
        self.session = None


def get_session_manager() -> SessionContextManager:
    return SessionContextManager()


def query_compile(
    query: Select | CTE | ReturningInsert | ReturningUpdate,
) -> SQLCompiler:
    """Метод вернет скомпилированный SQL-запрос. Используется для логирования.

    :param query: SQL-запрос
    :return :class:`SQLCompiler` - скомпилированный SQL-запрос.
    """
    sql_compile: SQLCompiler = query.compile(
        engine.engine, compile_kwargs={"literal_binds": True}
    )
    return sql_compile
