from src.dao.product import ProductDAO
from src.dao.property import PropertyDAO
from src.dao.property_group import PropertyGroupDAO
from src.rabbitmq.consumer import Consumer
from src.schemas.messages.rmq_product_schema import RmqProductSchema


class UpdateProducts:

    def __init__(self):
        self.consumer = Consumer()

    async def add_products_in_db(self) -> None:
        """Добавляет новые товары в БД из RMQ."""
        products: RmqProductSchema = await self.consumer.get_messages()
        for product in products.root:
            if await ProductDAO.find_one_or_none(name=product.name) is None:
                await ProductDAO.add(
                    id=product.id,
                    name=product.name,
                    description=product.description,
                    brand_name=product.brand_name,
                )
                for group in product.property_groups:
                    await PropertyGroupDAO.add(
                        id=group.id,
                        name=group.name,
                        product_id=product.id,
                    )
                    for property_info in group.property_data:
                        await PropertyDAO.add(
                            id=property_info.id,
                            name=property_info.name,
                            value=property_info.value,
                            description=property_info.description,
                            property_group_id=group.id,
                        )
