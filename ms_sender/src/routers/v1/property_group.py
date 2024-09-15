from fastapi import APIRouter, Path, Query
from fastapi_pagination import Page, paginate
from starlette import status

from src.dao.property_group import PropertyGroupDAO
from src.schemas.property_group_schema import PropertyGroupSchema
from src.utils.construct_data import construct_property_groups_with_relationships

property_group_router = APIRouter(
    prefix="/property_groups", tags=["Группы характеристик"]
)


@property_group_router.get(
    "/get_groups_with_property",
    name="Получение групп характеристик",
    status_code=status.HTTP_200_OK,
    response_model=Page[PropertyGroupSchema],
    description="Получение групп характеристик с содержанием.",
)
async def get_groups_with_property() -> Page[PropertyGroupSchema]:
    results = await PropertyGroupDAO.get_property_groups_with_relationships()
    return paginate(await construct_property_groups_with_relationships(results))


@property_group_router.get(
    "/search_groups_by_name",
    name="Поиск групп характеристик",
    status_code=status.HTTP_200_OK,
    response_model=Page[PropertyGroupSchema],
    description="Получение групп характеристик по имени.",
)
async def search_groups_by_name(
    property_group_name: str = Query(
        default="Видеокарта", description="Название группы характеристик"
    )
) -> Page[PropertyGroupSchema]:
    results = await PropertyGroupDAO.get_property_groups_with_relationships(
        name=property_group_name
    )
    return paginate(await construct_property_groups_with_relationships(results))


@property_group_router.get(
    "/{product_id}",
    name="Получение групп характеристик товара",
    status_code=status.HTTP_200_OK,
    response_model=PropertyGroupSchema,
    description="Получение групп характеристик товара по ID.",
)
async def product_property_groups(
    product_id: int = Path(description="Идентификатор продукта"),
) -> list[dict]:
    results = await PropertyGroupDAO.get_property_groups_with_relationships(
        product_id=product_id
    )
    return await construct_property_groups_with_relationships(results)
