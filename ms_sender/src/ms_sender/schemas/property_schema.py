from pydantic import BaseModel, Field, RootModel


class PropertySchema(BaseModel):
    id: int
    name: str
    value: str
    description: str | None
    property_group_id: int


class UnicPropertySchema(BaseModel):
    property_name: str = Field(alias="distinct")


class UnicPropertiesSchema(RootModel):
    root: list[UnicPropertySchema]


class PropertyPostSchema(BaseModel):
    name: str
    value: str
    description: str | None
    property_group_id: int


class PropertyPatchSchema(BaseModel):
    name: str | None = Field(default=None)
    value: str | None = Field(default=None)
    description: str | None = Field(default=None)
    property_group_id: int


class PropertyPatchResponseSchema(BaseModel):
    id: int
