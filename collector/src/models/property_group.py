from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class PropertyGroup(Base):
    __tablename__ = "property_group"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    product_id: Mapped[List[int]] = mapped_column(ForeignKey("product.id"))

    property: Mapped[List["Property"]] = relationship(
        back_populates="property_group"
    )  # noqa
    product: Mapped["Product"] = relationship(
        "Product", back_populates="property_group"
    )  # noqa

    def __str__(self):
        return (
            "{"
            + f'"id": "{self.id}", "name": "{self.name}"," product_id": "{self.product_id}"'
            + "}"
        )
