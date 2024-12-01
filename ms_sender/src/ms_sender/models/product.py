from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.ms_sender.database import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    brand_name: Mapped[str]
    description: Mapped[str]

    property_group: Mapped[List["PropertyGroup"]] = relationship(  # noqa
        "PropertyGroup",
        back_populates="product",
    )

    def __str__(self):
        return (
            "{" + f'"id": "{self.id}", "name": "{self.name}", '
            f'"brand_name": "{self.brand_name}", "description": "{self.description}"'
            + "}"
        )
