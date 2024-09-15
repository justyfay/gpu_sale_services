from typing import List, Optional

from pydantic import BaseModel, Field, RootModel


class PropertySchema(BaseModel):
    id: int
    name: str
    value: str
    description: Optional[str]


class UnicPropertySchema(BaseModel):
    property_name: str = Field(alias="distinct")


class UnicPropertiesSchema(RootModel):
    root: List[UnicPropertySchema]
