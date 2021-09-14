import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from products.database import Base


class ReservationStatus(str, enum.Enum):
    created = "created"
    confirmed = "confirmed"


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="reservations")

    price = Column(Integer)
    price_currency = Column(String)
    quantity = Column(Integer)

    status = Column(Enum(ReservationStatus))

    updated_at = Column(DateTime, server_onupdate=func.now(), server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Reservation {self.id}>"
