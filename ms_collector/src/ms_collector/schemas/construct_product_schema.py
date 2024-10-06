from pydantic import BaseModel


class PropertyData(BaseModel):
    id: int
    name: str
    value: str
    description: str


class PropertyGroupData(BaseModel):
    id: int
    name: str
    property_data: list[PropertyData]


class ConstructProductData(BaseModel):
    """Схема для представления данных по товарам из БД в виде модели."""

    id: int
    name: str
    brand_name: str
    description: str
    property_groups: list[PropertyGroupData]
