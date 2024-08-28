import uvicorn
from fastapi import FastAPI
from src.logger import get_logger

logger = get_logger()
app: FastAPI = FastAPI(
    title="Collector",
    summary="Микросервис для сбора данных по видеокартам из сторонних сервисов.",
    version="1.0.0",
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=8001)
