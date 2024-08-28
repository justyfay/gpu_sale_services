from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class Property(Base):
    __tablename__ = "property"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    value: Mapped[str]
    description: Mapped[Optional[str]]
    property_group_id: Mapped[int] = mapped_column(ForeignKey("property_group.id"))

    property_group: Mapped["PropertyGroup"] = relationship(
        back_populates="property"
    )  # noqa

    def __str__(self):
        return (
            "{"
            + f'"id": "{self.id}", "name": "{self.name}"," value": "{self.value}", description": "{self.description}"'
            + "}"
        )
