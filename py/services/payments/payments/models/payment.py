import enum

from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.sql import func

from payments.database import Base


class PaymentStatus(str, enum.Enum):
    created = "created"
    confirmed = "confirmed"


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer)
    amount = Column(Integer)
    currency = Column(String)

    status = Column(Enum(PaymentStatus))

    updated_at = Column(DateTime, server_onupdate=func.now(), server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Payment {self.id}>"
