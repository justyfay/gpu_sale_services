from fastapi import APIRouter, Path
from starlette import status

from src.ms_sender.dao.property import PropertyDAO
from src.ms_sender.exceptions import PropertyAddFailed, PropertyAlreadyExists
from src.ms_sender.schemas.property_schema import (
    PropertyPatchResponseSchema,
    PropertyPatchSchema,
    PropertyPostSchema,
    PropertySchema,
    UnicPropertiesSchema,
)

property_router = APIRouter(prefix="/property", tags=["Характеристики"])


@property_router.post(
    "",
    name="Добавление характеристики",
    status_code=status.HTTP_201_CREATED,
    response_model=PropertySchema,
)
async def add_property(property_data: PropertyPostSchema):
    if await PropertyDAO.find_one_or_none(
        property_group_id=property_data.property_group_id, name=property_data.name
    ):
        raise PropertyAlreadyExists
    result = await PropertyDAO.add(
        name=property_data.name,
        value=property_data.value,
        description=property_data.description,
        property_group_id=property_data.property_group_id,
    )
    if result is None:
        raise PropertyAddFailed
    return PropertySchema.model_construct(
        id=result["id"],
        name=property_data.name,
        value=property_data.value,
        description=property_data.description,
        property_group_id=property_data.property_group_id,
    )


@property_router.patch(
    "/{property_id}",
    name="Редактирование характеристики",
    status_code=status.HTTP_200_OK,
    response_model=PropertyPatchResponseSchema,
    description="Указание 'property_group_id' в теле запроса обязательно.",
)
async def edit_property_group(
    property_group_data: PropertyPatchSchema,
    property_id: int = Path(description="Идентификатор характеристики"),
):
    if await PropertyDAO.find_one_or_none(
        property_group_id=property_group_data.property_group_id,
        name=property_group_data.name,
    ):
        raise PropertyAlreadyExists
    result = await PropertyDAO.patch(
        obj_id=property_id, **property_group_data.model_dump(exclude_none=True)
    )
    return result


@property_router.get(
    "/get_count_property",
    name="Получение характеристик",
    status_code=status.HTTP_200_OK,
    response_model=UnicPropertiesSchema,
    description="Получение уникальных характеристик товаров.",
)
async def get_brands_with_count_products() -> UnicPropertiesSchema:
    return await PropertyDAO.get_unic_properties()
