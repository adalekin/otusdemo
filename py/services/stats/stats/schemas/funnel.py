import datetime

from pydantic import BaseModel


class FunnelDaily(BaseModel):
    clicks: int
    registrations: int
    revenue: int
    date: datetime.date

    class Config:
        orm_mode = True
