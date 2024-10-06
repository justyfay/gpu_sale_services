from typing import Sequence

from sqlalchemy import RowMapping

from ms_sender.schemas.product_schema import ProductInfoFullSchema, ProductsSchema
from ms_sender.schemas.property_group_schema import PropertyGroupSchema, PropertyGroupsSchema
from ms_sender.schemas.property_schema import PropertySchema


async def construct_updated_products_data_with_relationships(
    result_from_db: Sequence[RowMapping],
) -> list[dict]:
    return ProductsSchema.model_construct(
        root=[
            ProductInfoFullSchema.model_construct(
                id=product.id,
                name=product.name,
                brand_name=product.brand_name,
                description=product.description,
                property_group=[
                    PropertyGroupSchema.model_construct(
                        id=property_group.id,
                        name=property_group.name,
                        product_id=product.id,
                        property_data=[
                            PropertySchema.model_construct(
                                id=property_info.id,
                                name=property_info.name,
                                value=property_info.value,
                                description=property_info.description,
                                property_group_id=property_group.id,
                            )
                            for property_info in property_group.property
                        ],
                    )
                    for property_group in product.property_group
                ],
            )
            for product in result_from_db
        ],
    ).model_dump()


async def construct_property_groups_with_relationships(
    property_groups: Sequence[RowMapping],
) -> list[dict]:
    return PropertyGroupsSchema.model_construct(
        root=[
            PropertyGroupSchema.model_construct(
                id=property_group.id,
                name=property_group.name,
                product_id=property_group.product_id,
                property_data=[
                    PropertySchema.model_construct(
                        id=property_info.id,
                        name=property_info.name,
                        value=property_info.value,
                        description=property_info.description,
                        property_group_id=property_group.id,
                    )
                    for property_info in property_group.property
                ],
            )
            for property_group in property_groups
        ],
    ).model_dump()
