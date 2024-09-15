from typing import Any, Sequence, Type

from sqlalchemy import Result, RowMapping, select
from sqlalchemy.orm import selectinload

from src.dao.base import BaseDAO
from src.database import Base, get_session_manager, query_compile
from src.logger import get_logger
from src.models.property import Property  # noqa
from src.models.property_group import PropertyGroup

logger = get_logger()


class PropertyGroupDAO(BaseDAO):
    model: Type[Base] = PropertyGroup

    @classmethod
    async def get_property_groups_with_relationships(
        cls, **filter_by
    ) -> Sequence[RowMapping]:
        """Метод вернет из БД информацию по группам характеристик со связями из таблицы 'Property'."""
        query = (
            select(PropertyGroup)
            .filter_by(**filter_by)
            .options(selectinload(PropertyGroup.property))
        )
        async with get_session_manager() as manager:
            logger.debug(f"SQL Query: '{query_compile(query)}'")
            query_execute: Result[Any] = await manager.session.execute(query)
            result: Sequence[RowMapping] = query_execute.scalars().all()
            logger.info(f"Result: '{len(result)} property groups'.'")
            await manager.commit()
            return result
