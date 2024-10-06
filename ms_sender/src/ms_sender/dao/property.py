from typing import Any, Sequence

from sqlalchemy import Result, RowMapping, func, select

from ms_sender.dao.base import BaseDAO
from ms_sender.database import Base, get_session_manager, query_compile
from ms_sender.logger import get_logger
from ms_sender.models.property import Property
from ms_sender.schemas.property_schema import UnicPropertiesSchema

logger = get_logger()


class PropertyDAO(BaseDAO):
    model: type[Base] = Property

    @classmethod
    async def get_unic_properties(cls) -> UnicPropertiesSchema:
        query_unic_properties = select(func.distinct(Property.name)).group_by(Property.name)

        async with get_session_manager() as manager:
            logger.debug(f"SQL Query: '{query_compile(query_unic_properties)}'")
            query_execute: Result[tuple | Any] = await manager.session.execute(query_unic_properties)
            result: Sequence[RowMapping] = query_execute.mappings().all()
            logger.info(f"Result: '{result}'")
            await manager.commit()
            return UnicPropertiesSchema.model_validate(result)
