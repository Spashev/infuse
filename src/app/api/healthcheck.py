from fastapi import APIRouter, status
from fastapi.responses import Response

router = APIRouter()


@router.get('/healthcheck')
async def healthcheck() -> Response:
    return Response(status_code=status.HTTP_200_OK)
