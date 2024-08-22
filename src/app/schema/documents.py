from pydantic import BaseModel
from app.core.schemes import BaseSchema, BaseRequest
from typing import List


class ImageSchema(BaseSchema):
    id: int
    image_url: str
    document_id: int


class CreateDocument(BaseRequest):
    title: str
    description: str
    company: int


class DocumentSchema(BaseModel):
    id: int
    title: str
    description: str
    images: List[ImageSchema] = []
