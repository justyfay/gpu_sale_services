from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Property(BaseModel):
    name: str
    value: str
    description: str


class PropertiesGroupItem(BaseModel):
    name: str
    properties: List[Property]


class Product(BaseModel):
    name: str
    brand_name: str = Field(alias="brandCompanyName")
    properties_group: List[PropertiesGroupItem] = Field(alias="propertiesGroup")


class Products(BaseModel):
    product_info: Product = Field(alias="product")


class AdditionalProductDataSchema(BaseModel):
    """Схема дополнительной информации по товару."""

    data: List[Products]
