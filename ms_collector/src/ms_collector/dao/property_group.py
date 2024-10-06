from ms_collector.dao.base import BaseDAO
from ms_collector.database import Base
from ms_collector.models.property_group import PropertyGroup


class PropertyGroupDAO(BaseDAO):
    model: type[Base] = PropertyGroup
