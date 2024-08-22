from fastapi import APIRouter

from app.api import healthcheck
from app.api.company.handler import router as company_router
from app.api.document.handler import router as document_router
from app.api.category.handler import router as category_router

router = APIRouter()

router.include_router(healthcheck.router, prefix="")
router.include_router(company_router, prefix="/company")
router.include_router(document_router, prefix="/document")
router.include_router(category_router, prefix="/category")
