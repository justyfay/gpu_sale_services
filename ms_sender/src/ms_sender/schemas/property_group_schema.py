from pydantic import BaseModel, RootModel

from ms_sender.schemas.property_schema import PropertySchema


class PropertyGroupSchema(BaseModel):
    id: int
    name: str
    product_id: int
    property_data: list[PropertySchema]


class PropertyGroupsSchema(RootModel):
    root: list[PropertyGroupSchema]


class PropertyGroupPostSchema(BaseModel):
    name: str
    product_id: int


class PropertyGroupPatchSchema(BaseModel):
    name: str
    product_id: int


class PropertyGroupPatchResponseSchema(BaseModel):
    id: int
