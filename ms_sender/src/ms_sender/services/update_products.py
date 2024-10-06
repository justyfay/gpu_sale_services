from ms_sender.dao.product import ProductDAO
from ms_sender.dao.property import PropertyDAO
from ms_sender.dao.property_group import PropertyGroupDAO
from ms_sender.rabbitmq.consumer import Consumer
from ms_sender.schemas.messages.rmq_product_schema import RmqProductSchema


class UpdateProducts:
    def __init__(self) -> None:
        self.consumer = Consumer()

    async def add_products_in_db(self) -> None:
        """Добавляет новые товары в БД из RMQ."""
        products: RmqProductSchema = await self.consumer.get_messages()
        for product in products.root:
            if await ProductDAO.find_one_or_none(name=product.name) is None:
                added_product = await ProductDAO.add(
                    name=product.name,
                    description=product.description,
                    brand_name=product.brand_name,
                )
                for group in product.property_groups:
                    added_property_group = await PropertyGroupDAO.add(
                        name=group.name,
                        product_id=added_product["id"],
                    )
                    for property_info in group.property_data:
                        await PropertyDAO.add(
                            name=property_info.name,
                            value=property_info.value,
                            description=property_info.description,
                            property_group_id=added_property_group["id"],
                        )
