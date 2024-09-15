from fastapi import APIRouter
from starlette import status

from src.dao.property import PropertyDAO
from src.schemas.property_schema import UnicPropertiesSchema

property_router = APIRouter(prefix="/property", tags=["Характеристики"])


@property_router.get(
    "/get_count_property",
    name="Получение характеристик",
    status_code=status.HTTP_200_OK,
    response_model=UnicPropertiesSchema,
    description="Получение уникальных характеристик товаров.",
)
async def get_brands_with_count_products() -> UnicPropertiesSchema:
    return await PropertyDAO.get_unic_properties()
