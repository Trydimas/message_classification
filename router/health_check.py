from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get("")
async def health_check() -> PlainTextResponse:
    return PlainTextResponse("OK!")
