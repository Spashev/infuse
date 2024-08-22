from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base

from app.database.models.base import BaseModel


class Category(BaseModel):
    __tablename__ = 'categories'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    title: Mapped[String] = mapped_column(String(255))
    description: Mapped[Text] = mapped_column(Text)

    companies: Mapped[list["Company"]] = relationship(
        "Company",
        secondary="categories_companies",
        back_populates="categories"
    )


class CategoryCompany(BaseModel):
    __tablename__ = 'categories_companies'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('categories.id'))
    company_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('companies.id'))
