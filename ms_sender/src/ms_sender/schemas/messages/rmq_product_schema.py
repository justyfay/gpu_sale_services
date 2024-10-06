from pydantic import BaseModel, RootModel


class Property(BaseModel):
    id: int
    name: str
    value: str
    description: str | None


class PropertyGroup(BaseModel):
    id: int
    name: str
    property_data: list[Property]


class Product(BaseModel):
    id: int
    name: str
    brand_name: str
    description: str
    property_groups: list[PropertyGroup]


class RmqProductSchema(RootModel):
    root: list[Product]
