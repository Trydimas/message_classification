from pydantic import BaseModel
from constants.complaint_states import ComplaintStatus, ComplaintSentiment, ComplaintCategory


class ComplaintBase(BaseModel):
    status: ComplaintStatus | None
    sentiment: ComplaintSentiment | None
    category: ComplaintCategory | None


class ComplaintResp(ComplaintBase):
    id: int

    class Config:
        model_config = True


class ComplaintMessage(BaseModel):
    message: str
