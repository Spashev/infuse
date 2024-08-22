from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.database import get_dev_db
from app.schema.categories import Category, CreateCategory
from app.api.category.service import CategoryService
from app.api.category.repository import CategoryRepository

router = APIRouter(tags=["categories"])


def get_category_service(session: Session = Depends(get_dev_db)):
    category_repository = CategoryRepository(session)
    return CategoryService(category_repository)


@router.get("", response_model=list[Category])
async def get_categories(category_service: CategoryService = Depends(get_category_service)):
    return category_service.get_all_categories()


@router.post("", response_model=Category)
async def create_category(category: CreateCategory, category_service: CategoryService = Depends(get_category_service)):
    return category_service.create_category(category)
