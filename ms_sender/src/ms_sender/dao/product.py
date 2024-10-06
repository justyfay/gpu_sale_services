from typing import Any, Sequence

from sqlalchemy import Result, RowMapping, Select, select
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import func

from ms_sender.dao.base import BaseDAO
from ms_sender.database import Base, get_session_manager, query_compile
from ms_sender.logger import get_logger
from ms_sender.models.product import Product
from ms_sender.models.property import Property  # noqa
from ms_sender.models.property_group import PropertyGroup  # noqa
from ms_sender.schemas.brand_schema import BrandsSchema

logger = get_logger()


class ProductDAO(BaseDAO):
    model: type[Base] = Product

    @classmethod
    async def get_product_by_name(cls, product_name: str) -> Any:
        query_product_by_name: Select = select(Product).where(Product.name.like(f"%{product_name}%"))
        async with get_session_manager() as manager:
            logger.debug(f"SQL Query: '{query_compile(query_product_by_name)}'")
            query_execute: Result[tuple | Any] = await manager.session.execute(query_product_by_name)
            result: Sequence[RowMapping] = query_execute.scalars().all()
            logger.info(f"Result: '{result}'")
            await manager.commit()
            return result

    @classmethod
    async def get_updated_products_with_relationships(cls, **filter_by) -> Sequence[RowMapping]:
        """Метод вернет из БД информацию по товару со всеми связями из других таблиц."""
        query = (
            select(Product)
            .filter_by(**filter_by)
            .options(selectinload(Product.property_group).options(selectinload(PropertyGroup.property)))
        )
        async with get_session_manager() as manager:
            logger.debug(f"SQL Query: '{query_compile(query)}'")
            query_execute: Result[Any] = await manager.session.execute(query)
            result: Sequence[RowMapping] = query_execute.scalars().all()
            logger.info(f"Result: '{len(result)} products.'")
            await manager.commit()
            return result

    @classmethod
    async def get_brands_with_count_products(cls) -> BrandsSchema:
        query_product_brand_name = select(
            Product.brand_name, func.count(Product.id).label("count_products")
        ).group_by(
            Product.brand_name,
        )
        async with get_session_manager() as manager:
            logger.debug(f"SQL Query: '{query_compile(query_product_brand_name)}'")
            query_execute: Result[tuple | Any] = await manager.session.execute(query_product_brand_name)
            result: Sequence[RowMapping] = query_execute.mappings().all()
            logger.info(f"Result: '{result}'")
            await manager.commit()
            return BrandsSchema.model_validate(result)
