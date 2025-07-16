import enum


class ComplaintStatus(str, enum.Enum):
    open = "Open"
    closed = "Closed"


class ComplaintCategory(str, enum.Enum):
    technical = "Техническая"
    cost = "Оплата"
    another = "Другое"


class ComplaintSentiment(str, enum.Enum):
    negative = "negative"
    positive = "positive"
    neutral = "neutral"
    unknown = "unknown"
