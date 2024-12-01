from src.ms_collector.dao.base import BaseDAO
from src.ms_collector.database import Base
from src.ms_collector.models.property_group import PropertyGroup


class PropertyGroupDAO(BaseDAO):
    model: type[Base] = PropertyGroup
