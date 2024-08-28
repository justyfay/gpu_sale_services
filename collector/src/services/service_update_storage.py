from typing import List

from src.dao.product import ProductDAO
from src.dao.property import PropertyDAO
from src.dao.property_group import PropertyGroupDAO
from src.schemas.additional_product_data_schema import (
    AdditionalProductDataSchema,
    Products,
    PropertiesGroupItem,
    Property,
)
from src.utils.http_client import HttpClient


class ServiceUpdateStorage:
    """Класс сервиса, обновляющего в БД данные по существующим товарам."""

    def __init__(self):
        self.client = HttpClient()

    async def products(self) -> List[Products]:
        results: AdditionalProductDataSchema = (
            await self.client.get_additional_product_data_request()
        )
        return results.data

    @staticmethod
    async def _update_product_property(
        property_group_id: int, properties: List[Property]
    ) -> None:
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

    async def _update_product_property_groups(
        self, product_id: int, property_groups: List[PropertiesGroupItem]
    ) -> None:
        for property_group in property_groups:
            if (
                await PropertyGroupDAO.find_one_or_none(
                    name=property_group.name, product_id=product_id
                )
                is None
            ):
                update_property_group = await PropertyGroupDAO.add(
                    name=property_group.name,
                    product_id=product_id,
                )
                await self._update_product_property(
                    property_group_id=update_property_group.get("id"),
                    properties=property_group.properties,
                )

    async def update_products(self) -> None:
        for product in await self.products():
            product_info = await ProductDAO.find_one_or_none(
                name=product.product_info.name
            )
            if product_info is not None:
                await self._update_product_property_groups(
                    product_id=product_info.get("id"),
                    property_groups=product.product_info.properties_group,
                )
