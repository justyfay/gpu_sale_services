from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ms_sender.database import Base


class Property(Base):
    __tablename__ = "property"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    value: Mapped[str]
    description: Mapped[str | None]
    property_group_id: Mapped[int] = mapped_column(ForeignKey("property_group.id"))

    property_group: Mapped["PropertyGroup"] = relationship(  # noqa
        back_populates="property",
    )

    def __str__(self):
        return (
            "{" + f'"id": "{self.id}", "name": "{self.name}", '
            f'"value": "{self.value}", description": "{self.description}"' + "}"
        )
