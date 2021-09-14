from typing import Optional

from deeplinks import settings
from deeplinks.http import client


async def send_event_use_case(
    # Hit
    t: str,
    tid: str,
    cid: Optional[str] = None,
    cf1: Optional[str] = None,
    cf2: Optional[str] = None,
    cf3: Optional[str] = None,
    cf4: Optional[str] = None,
    cf5: Optional[str] = None,
    # Traffic Sources
    dr: Optional[str] = None,
    cn: Optional[str] = None,
    cs: Optional[str] = None,
    # Content Information
    dl: Optional[str] = None,
    dh: Optional[str] = None,
    # Session
    uip: Optional[str] = None,
    uua: Optional[str] = None,
):
    await client.post(
        url=f"{settings.EVENTS_URL}/events/",
        json={
            "t": t,
            "tid": tid,
            "cid": cid,
            "dr": dr,
            "cn": cn,
            "cs": cs,
            "dl": dl,
            "dh": dh,
            "uip": uip,
            "uua": uua,
            "cf1": cf1,
            "cf2": cf2,
            "cf3": cf3,
            "cf4": cf4,
            "cf5": cf5,
        },
    )
