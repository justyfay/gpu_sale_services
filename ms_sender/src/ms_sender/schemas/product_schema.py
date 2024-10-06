from pydantic import BaseModel, RootModel

from ms_sender.schemas.property_group_schema import PropertyGroupSchema


class ProductInfoBaseSchema(BaseModel):
    id: int
    name: str
    brand_name: str
    description: str


class ProductInfoFullSchema(ProductInfoBaseSchema):
    property_group: list[PropertyGroupSchema]


class ProductsSchema(RootModel):
    root: list[ProductInfoFullSchema]


class ProductPostSchema(BaseModel):
    name: str
    brand_name: str
    description: str


class ProductPatchSchema(BaseModel):
    name: str | None = None
    brand_name: str | None = None
    description: str | None = None


class ProductPatchResponseSchema(BaseModel):
    id: int
