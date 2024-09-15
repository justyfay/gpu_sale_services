from typing import Any, Sequence, Type

from sqlalchemy import Result, RowMapping, select
from sqlalchemy.orm import selectinload

from src.dao.base import BaseDAO
from src.database import Base, get_session_manager, query_compile
from src.logger import get_logger
from src.models.product import Product
from src.models.property import Property  # noqa
from src.models.property_group import PropertyGroup

logger = get_logger()


class ProductDAO(BaseDAO):
    model: Type[Base] = Product

    @staticmethod
    async def get_updated_products_with_relationships(
        **filter_by,
    ) -> Sequence[RowMapping]:
        """Метод вернет из БД информацию по товару со всеми связями из других таблиц."""
        query = (
            select(Product)
            .filter_by(**filter_by)
            .options(
                selectinload(Product.property_group).options(
                    selectinload(PropertyGroup.property)
                )
            )
        )
        async with get_session_manager() as manager:
            logger.debug(f"SQL Query: '{query_compile(query)}'")
            query_execute: Result[Any] = await manager.session.execute(query)
            result: Sequence[RowMapping] = query_execute.scalars().all()
            logger.info(f"Result: '{len(result)} products.'")
            await manager.commit()
        return result
