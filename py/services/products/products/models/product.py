from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from products.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    price_currency = Column(String)
    quantity = Column(Integer)

    reservations = relationship("Reservation", back_populates="product")

    def __repr__(self):
        return f"<Product {self.id}>"
