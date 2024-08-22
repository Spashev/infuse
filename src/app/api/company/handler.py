from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status, Response

from app.database import get_dev_db
from app.schema.companies import Company, CreateCompany
from app.database.models.companies import Company as CompanyModel
from app.database.models.categories import Category as CategoryModel

router = APIRouter(tags=["companies"])


@router.get("", response_model=list[Company])
async def get_companies(session: Session = Depends(get_dev_db)):
    companies = session.query(CompanyModel).all()
    return companies


@router.post("", response_model=Company)
async def create_company(company: CreateCompany, session: Session = Depends(get_dev_db)):
    try:
        company_model = CompanyModel(**company.model_dump(exclude={'categories'}))
        categories = session.query(CategoryModel).filter(CategoryModel.id.in_(company.categories)).all()
        if len(categories) == 0:
            return Response(
                content=f"Category with ID {company.categories} not found.",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        company_model.categories = categories

        session.add(company_model)
        session.commit()
        session.refresh(company_model)

        return company_model
    except Exception as e:
        return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)
