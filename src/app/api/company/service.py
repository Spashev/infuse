from app.api.company.repository import CompanyRepository
from app.schema.companies import CreateCompany
from fastapi import HTTPException, status


class CompanyService:
    def __init__(self, company_repository: CompanyRepository):
        self.company_repository = company_repository

    def get_all_companies(self):
        return self.company_repository.get_all_companies()

    def create_company(self, company: CreateCompany):
        return self.company_repository.create_company(company)
