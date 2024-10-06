from ms_collector.dao.base import BaseDAO
from ms_collector.database import Base
from ms_collector.models.property import Property


class PropertyDAO(BaseDAO):
    model: type[Base] = Property
