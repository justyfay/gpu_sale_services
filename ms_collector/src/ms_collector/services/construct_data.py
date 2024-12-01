from src.ms_collector.dao.product import ProductDAO
from src.ms_collector.schemas.construct_product_schema import (
    ConstructProductData,
    PropertyData,
    PropertyGroupData,
)
from src.ms_collector.services.service_addition_storage import ServiceAdditionStorage
from src.ms_collector.services.service_update_storage import ServiceUpdateStorage


class ConstructData:
    """Класс формирования данных из БД для отправки в брокер."""

    @staticmethod
    async def construct_product_data() -> list[dict]:
        await ServiceAdditionStorage().add_products()
        await ServiceUpdateStorage().update_products()
        products = await ProductDAO.get_updated_products_with_relationships(
            is_updated=True
        )
        products_data_json: list[dict] = []
        for product in products:
            product_model = ConstructProductData.model_construct(
                id=product.id,
                name=product.name,
                description=product.description,
                brand_name=product.brand_name,
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
