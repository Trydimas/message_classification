from fastapi import APIRouter, Depends
from services.complaint import get_classification_text
from database import get_session
from schema.complaint import ComplaintResp

router = APIRouter(
    prefix="message/"
)


@router.post("")
async def retrieve_message(session: Depends(get_session),
                           message: str
                           ) -> ComplaintResp:
    return await get_classification_text(session=session, text=message)


#TODO make end-point for get_list