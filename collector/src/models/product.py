from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    brand_name: Mapped[str]
    description: Mapped[str]

    property_group: Mapped[List["PropertyGroup"]] = relationship(
        "PropertyGroup", back_populates="product"
    )  # noqa

    def __str__(self):
        return (
            "{"
            + f'"id": "{self.id}", "name": "{self.name}", "brand_name": "{self.brand_name}", "description": "{self.description}"'
            + "}"
        )
