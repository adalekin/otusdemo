import datetime

from pydantic import BaseModel


class CreatePayment(BaseModel):
    order_id: int
    amount: int
    currency: str

    class Config:
        orm_mode = True


class Payment(CreatePayment):
    id: int
    status: str

    updated_at: datetime.datetime
    created_at: datetime.datetime

    class Config:
        orm_mode = True
