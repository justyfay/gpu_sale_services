from typing import List

from pydantic import BaseModel, RootModel

from src.schemas.property_group_schema import PropertyGroupSchema


class ProductInfoBaseSchema(BaseModel):
    id: int
    name: str
    brand_name: str
    description: str


class ProductInfoFullSchema(ProductInfoBaseSchema):
    property_group: List[PropertyGroupSchema]


class ProductsSchema(RootModel):
    root: List[ProductInfoFullSchema]
