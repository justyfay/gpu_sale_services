from typing import List

from pydantic import BaseModel, RootModel

from src.schemas.property_schema import PropertySchema


class PropertyGroupSchema(BaseModel):
    id: int
    name: str
    property_data: List[PropertySchema]


class PropertyGroupsSchema(RootModel):
    root: List[PropertyGroupSchema]
