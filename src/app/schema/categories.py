from app.core.schemes import BaseSchema, BaseRequest, BaseModel


class BaseCategory(BaseRequest):
    title: str
    description: str


class Category(BaseSchema, BaseCategory):
    ...


class CreateCategory(BaseCategory):
    ...
