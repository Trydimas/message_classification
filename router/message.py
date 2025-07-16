from fastapi import APIRouter, Depends

from services import complaint
from database import get_session
from schema.complaint import ComplaintResp, ComplaintMessage
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/message"
)


@router.post("/")
async def retrieve_message(message: ComplaintMessage,
                           session: AsyncSession = Depends(get_session),
                           ) -> ComplaintResp:
    return await complaint.get_classification_text(session=session, body=message)


@router.get("/")
async def get_all_complaints(session=Depends(get_session)):
    return await complaint.get_all_complaints(session)
