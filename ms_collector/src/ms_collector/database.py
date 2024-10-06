from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import CTE, DateTime, MetaData, Select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.sql.compiler import SQLCompiler
from sqlalchemy.sql.dml import ReturningInsert, ReturningUpdate

from ms_collector.config import settings
from ms_collector.logger import get_logger

logger = get_logger()

engine: AsyncEngine = create_async_engine(
    url=settings.database_url,
    pool_size=20,
    max_overflow=10,
    pool_recycle=3600,
    pool_pre_ping=True,
    execution_options={"schema_translate_map": {None: "collector"}},
)
async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base(metadata=MetaData(schema="collector"))


class BaseModel:
    """Базовая модель, от которой можно наследовать остальные модели."""

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC).replace(tzinfo=None))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC).replace(tzinfo=None))


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
    sql_compile: SQLCompiler = query.compile(engine.engine, compile_kwargs={"literal_binds": True})
    return sql_compile
