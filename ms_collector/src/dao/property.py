from typing import Type

from src.dao.base import BaseDAO
from src.database import Base
from src.models.property import Property


class PropertyDAO(BaseDAO):
    model: Type[Base] = Property
