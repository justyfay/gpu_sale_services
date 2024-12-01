from src.ms_collector.dao.base import BaseDAO
from src.ms_collector.database import Base
from src.ms_collector.models.property import Property


class PropertyDAO(BaseDAO):
    model: type[Base] = Property
