from typing import Any, Sequence, Tuple, Type

from sqlalchemy import Result, RowMapping, func, select

from src.dao.base import BaseDAO
from src.database import Base, get_session_manager, query_compile
from src.logger import get_logger
from src.models.property import Property
from src.schemas.property_schema import UnicPropertiesSchema

logger = get_logger()


class PropertyDAO(BaseDAO):
    model: Type[Base] = Property

    @classmethod
    async def get_unic_properties(cls) -> UnicPropertiesSchema:
        query_unic_properties = select(func.distinct(Property.name)).group_by(
            Property.name
        )

        async with get_session_manager() as manager:
            logger.debug(f"SQL Query: '{query_compile(query_unic_properties)}'")
            query_execute: Result[Tuple | Any] = await manager.session.execute(
                query_unic_properties
            )
            result: Sequence[RowMapping] = query_execute.mappings().all()
            logger.info(f"Result: '{result}'")
            await manager.commit()
            return UnicPropertiesSchema.model_validate(result)
