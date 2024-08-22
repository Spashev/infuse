from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.database.models.base import BaseModel


class Image(BaseModel):
    __tablename__ = 'images'

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, index=True)
    image_url: Mapped[String] = mapped_column(String(255))
    document_id: Mapped[Integer] = mapped_column(Integer, ForeignKey('documents.id'))

    document = relationship("Document", back_populates="images")
