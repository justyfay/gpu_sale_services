import asyncio
from typing import List

from src.dao.product import ProductDAO
from src.schemas.construct_product_schema import (
    ConstructProductData,
    PropertyData,
    PropertyGroupData,
)
from src.tasks.tasks import send_products


class Sender:
    @staticmethod
    async def construct_product_data() -> List[dict]:
        products = await ProductDAO.get_products_with_relationships()

        products_data_json: List[dict] = []
        for product in products:
            product_model = ConstructProductData.model_construct(
                id=product.id,
                name=product.name,
                description=product.description,
                property_groups=[
                    PropertyGroupData.model_construct(
                        id=property_group.id,
                        name=property_group.name,
                        property_data=[
                            PropertyData.model_construct(
                                id=property_info.id,
                                name=property_info.name,
                                value=property_info.value,
                                description=property_info.description,
                            )
                            for property_info in property_group.property
                        ],
                    )
                    for property_group in product.property_group
                ],
            ).model_dump()
            products_data_json.append(product_model)

        return products_data_json

    async def send_products(self):
        return send_products.delay(await self.construct_product_data())


asyncio.run(Sender().send_products())
