from fastapi import Query
from pydantic import BaseModel


class BaseRequest(BaseModel):
    class Config:
        populate_by_name = True


class BaseSchema(BaseModel):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
