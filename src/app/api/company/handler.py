from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_dev_db
from app.schema.companies import Company, CreateCompany
from app.api.company.service import CompanyService
from app.api.company.repository import CompanyRepository

router = APIRouter(tags=["companies"])


def get_company_service(session: Session = Depends(get_dev_db)):
    company_repository = CompanyRepository(session)
    return CompanyService(company_repository)


@router.get("", response_model=list[Company])
async def get_companies(company_service: CompanyService = Depends(get_company_service)):
    return company_service.get_all_companies()


@router.post("", response_model=Company)
async def create_company(company: CreateCompany, company_service: CompanyService = Depends(get_company_service)):
    return company_service.create_company(company)
