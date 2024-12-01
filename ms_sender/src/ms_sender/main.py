import uvicorn
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from fastapi_pagination.utils import disable_installed_extensions_check

from src.ms_sender.routers.__init__ import api_router

app: FastAPI = FastAPI(
    title="Sender",
    summary="Микросервис для отдачи данных по видеокартам.",
    version="1.0.0",
)
add_pagination(app)
disable_installed_extensions_check()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=8001)
