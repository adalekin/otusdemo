import datetime
from typing import Optional

from pydantic import BaseModel


class CreateEvent(BaseModel):
    # Hit
    t: str
    partner_id: str
    cid: str
    cf1: Optional[str] = None
    cf2: Optional[str] = None
    cf3: Optional[str] = None
    cf4: Optional[str] = None
    cf5: Optional[str] = None
    # Traffic Sources
    dr: Optional[str] = None
    cn: Optional[str] = None
    cs: Optional[str] = None
    # Content Information
    dl: Optional[str] = None
    dh: Optional[str] = None
    # Session
    uip: Optional[str] = None
    uua: Optional[str] = None


class Event(CreateEvent):
    created_at: datetime.datetime

    class Config:
        orm_mode = True
