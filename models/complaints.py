from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base
from constants.complaint_states import ComplaintStatus, ComplaintSentiment, ComplaintCategory


class ComplaintDB(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(255))
    status = Column(String, default=ComplaintStatus.open)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    sentiment = Column(String, default=ComplaintSentiment.unknown)
    category = Column(String, default=ComplaintCategory.another)
