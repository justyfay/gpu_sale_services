from fastapi import APIRouter, Query
from fastapi_pagination import Page, paginate
from starlette import status

from src.dao.product import ProductDAO
from src.schemas.brand_schema import BrandsSchema
from src.schemas.product_schema import ProductInfoBaseSchema, ProductInfoFullSchema
from src.utils.construct_data import construct_updated_products_data_with_relationships

product_router = APIRouter(prefix="/product", tags=["Товары"])


@product_router.get(
    "/search_by_name",
    name="Поиск товаров",
    status_code=status.HTTP_200_OK,
    response_model=Page[ProductInfoBaseSchema],
    description="Поиск товара по совпадению в названии.",
)
async def search_product_by_name(
    product_name: str = Query(default="RTX", description="Название товара")
) -> Page[ProductInfoBaseSchema]:
    result = await ProductDAO.get_product_by_name(product_name=product_name)
    return paginate(result)


@product_router.get(
    "/get_all_products_with_info",
    name="Получение всех товаров",
    status_code=status.HTTP_200_OK,
    response_model=Page[ProductInfoFullSchema],
    description="Получение всех товаров с характеристиками по каждому.",
)
async def get_all_products_with_info() -> Page[ProductInfoFullSchema]:
    result = await ProductDAO.get_updated_products_with_relationships()
    return paginate(await construct_updated_products_data_with_relationships(result))


@product_router.get(
    "/get_brands_with_count_products",
    name="Получение брендов",
    status_code=status.HTTP_200_OK,
    response_model=BrandsSchema,
    description="Получение всех брендов c количеством товаров.",
)
async def get_brands_with_count_products() -> BrandsSchema:
    return await ProductDAO.get_brands_with_count_products()
