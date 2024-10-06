from fastapi import APIRouter, Path, Query
from fastapi_pagination import Page, paginate
from starlette import status

from ms_sender.dao.property_group import PropertyGroupDAO
from ms_sender.exceptions import PropertyGroupAddFailed, PropertyGroupAlreadyExists
from ms_sender.schemas.property_group_schema import (
    PropertyGroupPatchResponseSchema,
    PropertyGroupPatchSchema,
    PropertyGroupPostSchema,
    PropertyGroupSchema,
    PropertyGroupsSchema,
)
from ms_sender.utils.construct_data import construct_property_groups_with_relationships

property_group_router = APIRouter(prefix="/property_groups", tags=["Группы характеристик"])


@property_group_router.post(
    "",
    name="Добавление группы характеристик",
    status_code=status.HTTP_200_OK,
    response_model=PropertyGroupSchema,
)
async def add_property_group(property_group_data: PropertyGroupPostSchema) -> None:
    if await PropertyGroupDAO.find_one_or_none(
        product_id=property_group_data.product_id, name=property_group_data.name
    ):
        raise PropertyGroupAlreadyExists

    result = await PropertyGroupDAO.add(
        name=property_group_data.name, product_id=property_group_data.product_id
    )
    if result is None:
        raise PropertyGroupAddFailed

    return PropertyGroupSchema.model_construct(
        id=result["id"],
        name=property_group_data.name,
        product_id=property_group_data.product_id,
    )


@property_group_router.patch(
    "/{property_group_id}",
    name="Редактирование группы характеристик",
    status_code=status.HTTP_200_OK,
    response_model=PropertyGroupPatchResponseSchema,
    description="Редактирование имени группы характеристик",
)
async def edit_property_group(
    property_group_data: PropertyGroupPatchSchema,
    property_group_id: int = Path(description="Идентификатор группы характеристик"),
) -> PropertyGroupPatchResponseSchema:
    if await PropertyGroupDAO.find_one_or_none(
        product_id=property_group_data.product_id, name=property_group_data.name
    ):
        raise PropertyGroupAlreadyExists
    result = await PropertyGroupDAO.patch(obj_id=property_group_id, **property_group_data.model_dump())
    return result


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
    property_group_name: str = Query(default="Видеокарта", description="Название группы характеристик"),
) -> Page[PropertyGroupSchema]:
    results = await PropertyGroupDAO.get_property_groups_with_relationships(name=property_group_name)
    return paginate(await construct_property_groups_with_relationships(results))


@property_group_router.get(
    "/{product_id}",
    name="Получение групп характеристик товара",
    status_code=status.HTTP_200_OK,
    response_model=PropertyGroupsSchema,
    description="Получение групп характеристик товара по ID.",
)
async def product_property_groups(
    product_id: int = Path(description="Идентификатор продукта"),
):
    results = await PropertyGroupDAO.get_property_groups_with_relationships(product_id=product_id)
    return await construct_property_groups_with_relationships(results)
