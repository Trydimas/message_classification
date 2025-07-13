from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base
from constants.complaint_states import ComplaintStatus, ComplaintSentiment, ComplaintCategory
from sqlalchemy.orm import class_mapper


class ComplaintDB(Base):
    __tablename__ = 'complaints'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(255))
    status = Column(String, default=ComplaintStatus.open)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    sentiment = Column(String, default=ComplaintSentiment.unknown)
    category = Column(String, default=ComplaintCategory.another)

    def as_dict(self):
        columns = class_mapper(self.__class__).mapped_table.c
        return {col.name: getattr(self, col.name) for col in columns}