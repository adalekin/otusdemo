import datetime

from pydantic import BaseModel


class CreateReservation(BaseModel):
    order_id: int
    product_id: int
    price: int
    price_currency: str
    quantity: int

    class Config:
        orm_mode = True


class Reservation(CreateReservation):
    id: int
    status: str

    updated_at: datetime.datetime
    created_at: datetime.datetime

    class Config:
        orm_mode = True
