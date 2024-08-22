from sqlalchemy.orm import Session
from app.database.models.companies import Company as CompanyModel
from app.database.models.categories import Category as CategoryModel
from app.schema.companies import CreateCompany
from fastapi import HTTPException, status


class CompanyRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_companies(self):
        return self.session.query(CompanyModel).all()

    def get_categories_by_ids(self, category_ids: list[int]):
        return self.session.query(CategoryModel).filter(CategoryModel.id.in_(category_ids)).all()

    def create_company(self, company: CreateCompany):
        categories = self.get_categories_by_ids(company.categories)
        if not categories:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category with ID {company.categories} not found."
            )

        company_model = CompanyModel(**company.model_dump(exclude={'categories'}))
        company_model.categories = categories

        self.session.add(company_model)
        self.session.commit()
        self.session.refresh(company_model)

        return company_model
