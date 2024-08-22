import os
from typing import List

from app.api.document.repository import DocumentRepository
from app.schema.documents import CreateDocument

from fastapi import UploadFile


class DocumentService:
    def __init__(self, document_repository: DocumentRepository):
        self.document_repository = document_repository

    def get_all_documents(self):
        return self.document_repository.get_all_documents()

    def create_document(
            self,
            title: str,
            description: str,
            company_id: int,
            files: List[UploadFile],
            upload_directory: str
    ):
        document_model = self.document_repository.create_document(title, description, company_id)

        for file in files:
            file_path = os.path.join(upload_directory, file.filename)
            with open(file_path, "wb") as buffer:
                buffer.write(file.file.read())

            self.document_repository.add_image_to_document(document_model.id, file_path)

        return document_model
