from fastapi import APIRouter, Depends
from services.complaint import get_classification_text
from database import get_session
from schema.complaint import ComplaintResp
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/message"
)


@router.post("/")
async def retrieve_message(message: str,
                           session:AsyncSession = Depends(get_session),
                           ) -> ComplaintResp:
    return await get_classification_text(session=session, text=message)


#TODO make end-point for get_list