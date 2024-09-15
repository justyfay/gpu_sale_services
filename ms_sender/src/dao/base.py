from typing import Any, Optional, Tuple, Type

from sqlalchemy import Result, RowMapping, Select, insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.dml import ReturningInsert

from src.database import Base, get_session_manager, query_compile
from src.logger import get_logger

logger = get_logger()


class BaseDAO:
    model: Type[Base] = None

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> Optional[RowMapping]:
        async with get_session_manager() as manager:
            query: Select[Tuple | Any] = select(cls.model.__table__.columns).filter_by(
                **filter_by
            )
            logger.debug(f"SQL Query: '{query_compile(query)}'")
            query_execute: Result[Tuple | Any] = await manager.session.execute(query)
            result: Optional[RowMapping] = query_execute.mappings().one_or_none()
            logger.info(f"Result: '{result}'")
            return result

    @classmethod
    async def add(cls, **data) -> Optional[RowMapping] | None:
        msg: str = ""
        try:
            query: ReturningInsert[Tuple | Any] = (
                insert(cls.model).values(**data).returning(cls.model.id)  # noqa
            )
            logger.debug(f"SQL Query: '{query_compile(query)}'")
            async with get_session_manager() as manager:
                query_execute: Result[Tuple | Any] = await manager.session.execute(
                    query
                )
                result: Optional[RowMapping] = query_execute.mappings().first()
                logger.info(f"Result: '{result}'")
                await manager.session.commit()
                return result
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg: str = (
                    "Database Exc: Cannot insert data into table. Details: {}".format(e)
                )
            elif isinstance(e, Exception):
                msg: str = (
                    "Unknown Exc: Cannot insert data into table. Details: {}".format(e)
                )

            logger.error(msg, extra={"table": cls.model.__tablename__}, exc_info=True)
            return None
