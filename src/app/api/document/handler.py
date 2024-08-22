import os
from typing import List

from fastapi import UploadFile, File, APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.core import settings
from app.database import get_dev_db
from app.schema.documents import DocumentSchema, CreateDocument
from app.database.models.companies import Company as CompanyModel
from app.database.models.documents import Document as DocumentModel
from app.database.models.images import Image

router = APIRouter(tags=["documents"])


@router.get("", response_model=List[DocumentSchema])
async def get_documents(session: Session = Depends(get_dev_db)):
    documents = session.query(DocumentModel).all()
    return documents


@router.post("", response_model=DocumentSchema)
async def create_document(
        title: str,
        description: str,
        company: int,
        files: List[UploadFile] = File(...),
        session: Session = Depends(get_dev_db)
):
    try:
        company_instance = session.query(CompanyModel).filter(CompanyModel.id == company).first()
        if not company_instance:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Company with ID {company} not found."
            )

        document_model = DocumentModel(
            title=title,
            description=description,
            company_id=company_instance.id
        )
        session.add(document_model)
        session.commit()
        session.refresh(document_model)

        for file in files:
            file_path = os.path.join(settings.UPLOAD_DIRECTORY, file.filename)
            print(file_path, settings.UPLOAD_DIRECTORY)
            with open(file_path, "wb") as buffer:
                buffer.write(await file.read())

            image_model = Image(
                image_url=file_path,
                document_id=document_model.id
            )
            session.add(image_model)

        session.commit()
        session.refresh(document_model)

        return document_model
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
