from __future__ import annotations

from pydantic import BaseModel, Field


class Property(BaseModel):
    name: str
    value: str
    description: str | None = Field(alias="nameDescription")


class PropertiesGroupItem(BaseModel):
    name: str
    properties: list[Property]


class Properties(BaseModel):
    property_groups: list[PropertiesGroupItem] = Field(alias="key")


class Product(BaseModel):
    name: str
    brand_name: str = Field(alias="brandName")
    description: str
    properties: Properties


class MainProductDataSchema(BaseModel):
    """Схема основной информации по товару."""

    data: list[Product] = Field(alias="body")
