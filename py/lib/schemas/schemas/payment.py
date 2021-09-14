import datetime

from pydantic import BaseModel


class PaymentConfirmed(BaseModel):
    id: int
    order_id: int
    amount: int
    currency: str
    status: str

    updated_at: datetime.datetime
    created_at: datetime.datetime
