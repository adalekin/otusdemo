import datetime
from typing import Optional

from pydantic import BaseModel


class EventFired(BaseModel):
    # Hit
    t: str
    partner_id: str
    cid: str
    created_at: datetime.datetime

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
    # Event
    ec: Optional[str] = None
    ea: Optional[str] = None
    el: Optional[str] = None
    ev: Optional[int] = None
