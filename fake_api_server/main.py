import uvicorn
from fastapi import FastAPI, APIRouter
from starlette import status

from heplers.data.country_link_data import country_link_data
from heplers.data.net_video_data import net_video_data

app: FastAPI = FastAPI(
    title="FakeApiServer",
    summary="Сервер с фейковыми API.",
    description="Содержит в себе несколько фейковых эндпоинтов, которые отдают данные по видеокартам.",
    version="1.0.0",
)

net_video_router = APIRouter(
    prefix="/net_video",
    tags=["Fake API 'NetVideo'."],
)


@net_video_router.get(
    path="/products/graphic_cards/list",
    status_code=status.HTTP_200_OK,
    summary="Список видеокарт фейкового магазина 'NetVideo'.",
    description="Метод отдает список видеокарт с техническими характеристиками.",
)
async def net_video_graphic_cards() -> dict:
    return {
        "success": True,
        "messages": [],
        "body": net_video_data(),
        "count": len(net_video_data())
    }


country_link_router = APIRouter(
    prefix="/country_link",
    tags=["Fake API 'CountryLink'."],
)


@country_link_router.get(
    path="/catalog/gpu_cards/list",
    status_code=status.HTTP_200_OK,
    summary="Список видеокарт фейкового магазина 'CountryLink'.",
    description="Метод отдает список видеокарт с техническими характеристиками товара, которых нет в эндпоинте "
                "'NetVideo' (доступное разрешение, охлаждение, вентиляторы, интерфейсы и т.д).",
)
async def country_link_graphic_cards() -> dict:
    return {
        "data": country_link_data(),
        "count": len(country_link_data())
    }


app.include_router(net_video_router)
app.include_router(country_link_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)