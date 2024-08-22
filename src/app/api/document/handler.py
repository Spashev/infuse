from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status

from app.database import get_dev_db
from app.schema.documents import DocumentSchema
from app.api.document.service import DocumentService
from app.api.document.repository import DocumentRepository
from app.core import settings

router = APIRouter(tags=["documents"])


def get_document_service(session: Session = Depends(get_dev_db)):
    document_repository = DocumentRepository(session)
    return DocumentService(document_repository)


@router.get("", response_model=List[DocumentSchema])
async def get_documents(document_service: DocumentService = Depends(get_document_service)):
    return document_service.get_all_documents()


@router.post("", response_model=DocumentSchema)
async def create_document(
        title: str,
        description: str,
        company: int,
        files: List[UploadFile] = File(...),
        document_service: DocumentService = Depends(get_document_service)
):
    try:
        return document_service.create_document(
            title=title,
            description=description,
            company_id=company,
            files=files,
            upload_directory=settings.UPLOAD_DIRECTORY
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
