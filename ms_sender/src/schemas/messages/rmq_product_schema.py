from typing import List, Optional

from pydantic import BaseModel, RootModel


class Property(BaseModel):
    id: int
    name: str
    value: str
    description: Optional[str]


class PropertyGroup(BaseModel):
    id: int
    name: str
    property_data: List[Property]


class Product(BaseModel):
    id: int
    name: str
    brand_name: str
    description: str
    property_groups: List[PropertyGroup]


class RmqProductSchema(RootModel):
    root: List[Product]
