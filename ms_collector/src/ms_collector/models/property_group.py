from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.ms_collector.database import Base


class PropertyGroup(Base):
    __tablename__ = "property_group"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    product_id: Mapped[list[int]] = mapped_column(ForeignKey("product.id"))

    property: Mapped[List["Property"]] = relationship(  # noqa
        back_populates="property_group",
    )
    product: Mapped["Product"] = relationship(  # noqa
        "Product",
        back_populates="property_group",
    )

    def __str__(self):
        return (
            "{"
            + f'"id": "{self.id}", "name": "{self.name}"," product_id": "{self.product_id}"'
            + "}"
        )
