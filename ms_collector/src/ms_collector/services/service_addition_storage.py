from ms_collector.dao.product import ProductDAO
from ms_collector.dao.property import PropertyDAO
from ms_collector.dao.property_group import PropertyGroupDAO
from ms_collector.schemas.main_product_data_schema import (
    MainProductDataSchema,
    Product,
    PropertiesGroupItem,
    Property,
)
from ms_collector.utils.http_client import HttpClient


class ServiceAdditionStorage:
    """Класс сервиса, добавляющего в БД данные по товарам."""

    def __init__(self):
        self.client = HttpClient()

    async def products(self) -> list[Product]:
        results: MainProductDataSchema = await self.client.get_main_product_data_request()
        return results.data

    @staticmethod
    async def _add_product_property(property_group_id: int, properties: list[Property]) -> None:
        for property_item in properties:
            if (
                await PropertyDAO.find_one_or_none(
                    property_group_id=property_group_id, name=property_item.name
                )
                is None
            ):
                await PropertyDAO.add(
                    name=property_item.name,
                    value=property_item.value,
                    description=property_item.description,
                    property_group_id=property_group_id,
                )

    async def _add_product_property_groups(
        self, product_id: int, property_groups: list[PropertiesGroupItem]
    ) -> None:
        for property_group in property_groups:
            if (
                await PropertyGroupDAO.find_one_or_none(name=property_group.name, product_id=product_id)
                is None
            ):
                insert_property_group = await PropertyGroupDAO.add(
                    name=property_group.name,
                    product_id=product_id,
                )
                await self._add_product_property(
                    property_group_id=insert_property_group.get("id"),
                    properties=property_group.properties,
                )

    async def add_products(self) -> list[Product]:
        for product in await self.products():
            if await ProductDAO.find_one_or_none(name=product.name) is None:
                insert_product = await ProductDAO.add(
                    name=product.name,
                    brand_name=product.brand_name,
                    description=product.description,
                )
                await self._add_product_property_groups(
                    product_id=insert_product.get("id"),
                    property_groups=product.properties.property_groups,
                )
        return await self.products()
