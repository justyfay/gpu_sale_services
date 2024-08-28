from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Property(BaseModel):
    name: str
    value: str
    description: Optional[str] = Field(alias="nameDescription")


class PropertiesGroupItem(BaseModel):
    name: str
    properties: List[Property]


class Properties(BaseModel):
    property_groups: List[PropertiesGroupItem] = Field(alias="key")


class Product(BaseModel):
    name: str
    brand_name: str = Field(alias="brandName")
    description: str
    properties: Properties


class MainProductDataSchema(BaseModel):
    """Схема основной информации по товару."""

    data: List[Product] = Field(alias="body")
