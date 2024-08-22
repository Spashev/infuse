from typing import List

from app.core.schemes import BaseSchema, BaseRequest, BaseModel


class BaseCompany(BaseRequest):
    title: str
    description: str
    site_url: str


class Company(BaseSchema, BaseCompany):
    ...


class CreateCompany(BaseCompany):
    categories: List[int]
