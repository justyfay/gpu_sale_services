from fastapi import HTTPException
from starlette import status


class SenderException(HTTPException):
    status_code: int = 500
    detail: str = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class ProductAlreadyExists(SenderException):
    status_code: int = status.HTTP_409_CONFLICT
    detail: str = "Товар с таким именем уже существует"


class ProductNotExists(SenderException):
    status_code: int = status.HTTP_409_CONFLICT
    detail: str = "Данного товара не существует"


class ProductAddFailed(SenderException):
    status_code: int = status.HTTP_409_CONFLICT
    detail: str = "Ошибка при добавлении продукта"


class PropertyGroupAlreadyExists(SenderException):
    status_code: int = status.HTTP_409_CONFLICT
    detail: str = (
        "Группа характеристик с таким именем для указанного товара уже существует"
    )


class PropertyGroupAddFailed(SenderException):
    status_code: int = status.HTTP_409_CONFLICT
    detail: str = "Ошибка при добавлении группы характеристик"


class PropertyAddFailed(SenderException):
    status_code: int = status.HTTP_409_CONFLICT
    detail: str = "Ошибка при добавлении характеристики"


class PropertyAlreadyExists(SenderException):
    status_code: int = status.HTTP_409_CONFLICT
    detail: str = "Такая характеристика для данной группы уже существует"
