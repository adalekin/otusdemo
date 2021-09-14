from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: int
    price_currency: str
    quantity: int

    class Config:
        orm_mode = True
