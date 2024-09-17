from typing import List

from pydantic import BaseModel, RootModel

from src.schemas.property_schema import PropertySchema


class PropertyGroupSchema(BaseModel):
    id: int
    name: str
    product_id: int
    property_data: List[PropertySchema]


class PropertyGroupsSchema(RootModel):
    root: List[PropertyGroupSchema]


class PropertyGroupPostSchema(BaseModel):
    name: str
    product_id: int


class PropertyGroupPatchSchema(BaseModel):
    name: str
    product_id: int


class PropertyGroupPatchResponseSchema(BaseModel):
    id: int
