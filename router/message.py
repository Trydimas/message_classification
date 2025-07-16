from fastapi import APIRouter, Depends
from services import complaint
from database import get_session
from schema.complaint import ComplaintResp
from sqlalchemy.ext.asyncio import AsyncSession
from models.complaints import ComplaintDB

router = APIRouter(
    prefix="/message"
)


@router.post("/")
async def retrieve_message(message: str,
                           session:AsyncSession = Depends(get_session),
                           ) -> ComplaintResp:
    return await complaint.get_classification_text(session=session, text=message)



@router.get("/")
async def get_all_complaints(session = Depends(get_session)) -> list[ComplaintDB]:
    return await complaint.get_all_complaints(session)
