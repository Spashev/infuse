import os
from sqlalchemy.orm import Session

from app.database.models.documents import Document as DocumentModel
from app.database.models.companies import Company as CompanyModel
from app.database.models.images import Image
from app.schema.documents import CreateDocument


class DocumentRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_documents(self):
        return self.session.query(DocumentModel).all()

    def get_company_by_id(self, company_id: int):
        return self.session.query(CompanyModel).filter(CompanyModel.id == company_id).first()

    def create_document(self, title: str, description: str, company_id: int):
        company_instance = self.get_company_by_id(company_id)
        if not company_instance:
            raise ValueError(f"Company with ID {company_id} not found.")

        document_model = DocumentModel(
            title=title,
            description=description,
            company_id=company_instance.id
        )
        self.session.add(document_model)
        self.session.commit()
        self.session.refresh(document_model)
        return document_model

    def add_image_to_document(self, document_id: int, file_path: str):
        image_model = Image(
            image_url=file_path,
            document_id=document_id
        )
        self.session.add(image_model)
        self.session.commit()
        self.session.refresh(image_model)
