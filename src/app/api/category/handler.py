from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_dev_db
from app.schema.categories import Category, CreateCategory
from app.database.models.categories import Category as CategoryModel

router = APIRouter(tags=["category"])


@router.get("", response_model=list[Category])
async def get_companies(session: Session = Depends(get_dev_db)):
    categories = session.query(CategoryModel).all()
    return categories


@router.post("", response_model=Category)
async def create_company(company: CreateCategory, session: Session = Depends(get_dev_db)):
    category_model = CategoryModel(**company.dict(exclude={'categories'}))
    session.add(category_model)
    session.commit()
    session.refresh(category_model)

    return category_model

