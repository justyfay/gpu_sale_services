from typing import Dict, List, Sequence

from sqlalchemy import RowMapping

from src.schemas.product_schema import ProductInfoFullSchema, ProductsSchema
from src.schemas.property_group_schema import PropertyGroupSchema, PropertyGroupsSchema
from src.schemas.property_schema import PropertySchema


async def construct_updated_products_data_with_relationships(
    result_from_db: Sequence[RowMapping],
) -> List[Dict]:
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
                        property_data=[
                            PropertySchema.model_construct(
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
            )
            for product in result_from_db
        ]
    ).model_dump()


async def construct_property_groups_with_relationships(
    property_groups: Sequence[RowMapping],
) -> List[Dict]:
    return PropertyGroupsSchema.model_construct(
        root=[
            PropertyGroupSchema.model_construct(
                id=property_group.id,
                name=property_group.name,
                property_data=[
                    PropertySchema.model_construct(
                        id=property_info.id,
                        name=property_info.name,
                        value=property_info.value,
                        description=property_info.description,
                    )
                    for property_info in property_group.property
                ],
            )
            for property_group in property_groups
        ]
    ).model_dump()
