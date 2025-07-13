from pydantic import BaseModel
from datetime import datetime
from constants.complaint_states import ComplaintStatus, ComplaintSentiment, ComplaintCategory


class ComplaintBase(BaseModel):
    status: ComplaintStatus | None
    sentiment: ComplaintSentiment | None
    category: ComplaintCategory | None


class ComplaintModel(ComplaintBase):
    text: str
    created_on: datetime | None

    class Config:
        model_config = True


class ComplaintResp(ComplaintBase):
    id: int

    class Config:
        model_config = True
