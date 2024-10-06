from fastapi import APIRouter

from ms_sender.routers.v1.product import product_router
from ms_sender.routers.v1.property import property_router
from ms_sender.routers.v1.property_group import property_group_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(product_router)
v1_router.include_router(property_group_router)
v1_router.include_router(property_router)
