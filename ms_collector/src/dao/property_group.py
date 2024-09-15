from typing import Type

from src.dao.base import BaseDAO
from src.database import Base
from src.models.property_group import PropertyGroup


class PropertyGroupDAO(BaseDAO):
    model: Type[Base] = PropertyGroup
