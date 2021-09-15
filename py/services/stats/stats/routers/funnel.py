from typing import List

from fastapi import APIRouter
from fastapi.params import Header

from stats import schemas
from stats.use_cases.funnel import get_funnel_daily_use_case

from .utils import get_jwt_payload

router = APIRouter()


@router.get("/funnel/daily/", tags=["funnel"], status_code=200, response_model=List[schemas.FunnelDaily])
async def get_funnel_daily(x_jwt_payload: str = Header(None)):
    payload = get_jwt_payload(x_jwt_payload)

    return get_funnel_daily_use_case(user_id=payload["user_id"])
