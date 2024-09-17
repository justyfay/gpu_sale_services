from typing import List, Optional

from pydantic import BaseModel, Field, RootModel


class PropertySchema(BaseModel):
    id: int
    name: str
    value: str
    description: Optional[str]
    property_group_id: int


class UnicPropertySchema(BaseModel):
    property_name: str = Field(alias="distinct")


class UnicPropertiesSchema(RootModel):
    root: List[UnicPropertySchema]


class PropertyPostSchema(BaseModel):
    name: str
    value: str
    description: Optional[str]
    property_group_id: int


class PropertyPatchSchema(BaseModel):
    name: Optional[str] = Field(default=None)
    value: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    property_group_id: int


class PropertyPatchResponseSchema(BaseModel):
    id: int
