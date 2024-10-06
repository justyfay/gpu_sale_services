from typing import Any

from sqlalchemy import Result, RowMapping, Select, insert, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.dml import ReturningInsert, ReturningUpdate

from ms_collector.database import Base, get_session_manager, query_compile
from ms_collector.logger import get_logger

logger = get_logger()


class BaseDAO:
    model: type[Base] = None

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> RowMapping | None:
        async with get_session_manager() as manager:
            query: Select[tuple | Any] = select(cls.model.__table__.columns).filter_by(**filter_by)
            logger.debug(f"SQL Query: '{query_compile(query)}'")
            query_execute: Result[tuple | Any] = await manager.session.execute(query)
            result: RowMapping | None = query_execute.mappings().one_or_none()
            logger.info(f"Result: '{result}'")
            return result

    @classmethod
    async def patch(cls, product_name: str, **data) -> RowMapping:
        async with get_session_manager() as manager:
            query: ReturningUpdate[tuple | Any] = (
                update(cls.model)
                .values(**data)
                .where(cls.model.name == product_name)  # noqa
                .returning(cls.model.id)  # noqa
            )
            logger.debug(f"SQL Query: '{query_compile(query)}'")
            query_execute: Result[tuple | Any] = await manager.session.execute(query)
            result: RowMapping | None = query_execute.mappings().first()
            logger.info(f"Result: '{result}'")
            await manager.session.commit()
            return result

    @classmethod
    async def add(cls, **data) -> RowMapping | None | None:
        msg: str = ""
        try:
            query: ReturningInsert[tuple | Any] = (
                insert(cls.model).values(**data).returning(cls.model.id)  # noqa
            )
            logger.debug(f"SQL Query: '{query_compile(query)}'")
            async with get_session_manager() as manager:
                query_execute: Result[tuple | Any] = await manager.session.execute(query)
                result: RowMapping | None = query_execute.mappings().first()
                logger.info(f"Result: '{result}'")
                await manager.session.commit()
                return result
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg: str = "Database Exc: Cannot insert data into table. Details: {}".format(e)
            elif isinstance(e, Exception):
                msg: str = "Unknown Exc: Cannot insert data into table. Details: {}".format(e)

            logger.error(msg, extra={"table": cls.model.__tablename__}, exc_info=True)
            return None
