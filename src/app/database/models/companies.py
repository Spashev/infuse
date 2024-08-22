from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base

from app.database.models.base import BaseModel


class Company(BaseModel):
    __tablename__ = 'companies'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    site_url: Mapped[String] = mapped_column(String(255))
    title: Mapped[String] = mapped_column(String(255))
    description: Mapped[Text] = mapped_column(Text)

    documents = relationship("Document", back_populates="company")
    categories: Mapped[list["Category"]] = relationship(
        "Category",
        secondary="categories_companies",
        back_populates="companies"
    )
