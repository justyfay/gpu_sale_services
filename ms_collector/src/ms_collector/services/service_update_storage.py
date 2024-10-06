from ms_collector.dao.product import ProductDAO
from ms_collector.dao.property import PropertyDAO
from ms_collector.dao.property_group import PropertyGroupDAO
from ms_collector.schemas.additional_product_data_schema import (
    AdditionalProductDataSchema,
    Products,
    PropertiesGroupItem,
    Property,
)
from ms_collector.utils.http_client import HttpClient


class ServiceUpdateStorage:
    """Класс сервиса, обновляющего в БД данные по существующим товарам."""

    def __init__(self):
        self.client = HttpClient()

    async def products(self) -> list[Products]:
        results: AdditionalProductDataSchema = await self.client.get_additional_product_data_request()
        return results.data

    @staticmethod
    async def _update_product_property(property_group_id: int, properties: list[Property]) -> None:
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
        self,
        product_id: int,
        property_groups: list[PropertiesGroupItem],
    ) -> None:
        for property_group in property_groups:
            if (
                await PropertyGroupDAO.find_one_or_none(name=property_group.name, product_id=product_id)
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
            product_info = await ProductDAO.find_one_or_none(name=product.product_info.name)
            if product_info is not None:
                await self._update_product_property_groups(
                    product_id=product_info.get("id"),
                    property_groups=product.product_info.properties_group,
                )
                await ProductDAO.patch(product_name=product.product_info.name, is_updated=True)
