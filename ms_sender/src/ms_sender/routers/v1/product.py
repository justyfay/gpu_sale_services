from fastapi import APIRouter, Path, Query
from fastapi_pagination import Page, paginate
from starlette import status

from src.ms_sender.dao.product import ProductDAO
from src.ms_sender.exceptions import (
    ProductAddFailed,
    ProductAlreadyExists,
    ProductNotExists,
)
from src.ms_sender.schemas.brand_schema import BrandsSchema
from src.ms_sender.schemas.product_schema import (
    ProductInfoBaseSchema,
    ProductInfoFullSchema,
    ProductPatchResponseSchema,
    ProductPatchSchema,
    ProductPostSchema,
    ProductsSchema,
)
from src.ms_sender.utils.construct_data import (
    construct_updated_products_data_with_relationships,
)

product_router = APIRouter(prefix="/product", tags=["Товары"])


@product_router.post(
    "",
    name="Добавление продукта",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductInfoBaseSchema,
)
async def add_product(product_data: ProductPostSchema) -> ProductInfoBaseSchema:
    if await ProductDAO.find_one_or_none(name=product_data.name):
        raise ProductAlreadyExists
    result = await ProductDAO.add(
        name=product_data.name,
        brand_name=product_data.brand_name,
        description=product_data.description,
    )
    if result is None:
        raise ProductAddFailed
    return ProductInfoBaseSchema.model_construct(
        id=result["id"],
        name=product_data.name,
        brand_name=product_data.brand_name,
        description=product_data.description,
    )


@product_router.patch(
    "/{product_id}",
    name="Редактирование продукта",
    status_code=status.HTTP_200_OK,
    response_model=ProductPatchResponseSchema,
)
async def edit_product(
    product_data: ProductPatchSchema,
    product_id: int = Path(description="Идентификатор продукта"),
) -> ProductPatchResponseSchema:
    current_product = await ProductDAO.find_one_or_none(id=product_id)
    if current_product is None:
        raise ProductNotExists
    result = await ProductDAO.patch(
        obj_id=product_id, **product_data.model_dump(exclude_none=True)
    )
    return ProductPatchResponseSchema.model_validate(result)


@product_router.get(
    "/search_by_name",
    name="Поиск товаров",
    status_code=status.HTTP_200_OK,
    response_model=Page[ProductInfoBaseSchema],
    description="Поиск товара по совпадению в названии.",
)
async def search_product_by_name(
    product_name: str = Query(default="RTX", description="Название товара"),
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


@product_router.get(
    "/{product_id}",
    name="Получение продукта",
    status_code=status.HTTP_200_OK,
    response_model=ProductsSchema,
    description="Получение продукта по ID.",
)
async def get_product_by_id(
    product_id: int = Path(description="Идентификатор продукта"),
) -> ProductsSchema:
    result = await ProductDAO.get_updated_products_with_relationships(id=product_id)

    construct_result_data = await construct_updated_products_data_with_relationships(
        result
    )
    return ProductsSchema.model_validate(construct_result_data)
