from pydantic import BaseModel, RootModel


class BrandSchema(BaseModel):
    brand_name: str
    count_products: int


class BrandsSchema(RootModel):
    root: list[BrandSchema]
