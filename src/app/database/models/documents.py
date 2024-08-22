from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import BaseModel


class Document(BaseModel):
    __tablename__ = 'documents'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    title: Mapped[String] = mapped_column(String(255))
    description: Mapped[Text] = mapped_column(Text)
    company_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('companies.id'))

    company = relationship("Company", back_populates="documents")
    images = relationship("Image", back_populates="document")
