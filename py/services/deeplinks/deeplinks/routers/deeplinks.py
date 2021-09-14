from typing import List

from fastapi import APIRouter
from fastapi.params import Header

from deeplinks import schemas
from deeplinks.use_cases.deeplink import create_deeplink_use_case, list_deeplinks_use_case

from .utils import get_jwt_payload

router = APIRouter()


@router.post("/deeplinks/", tags=["deeplinks"], response_model=schemas.Deeplink)
async def create_deeplink(create_deeplink: schemas.CreateDeeplink, x_jwt_payload: str = Header(None)):
    payload = get_jwt_payload(x_jwt_payload)

    return create_deeplink_use_case(user_id=payload["user_id"], create_deeplink=create_deeplink)


@router.get("/deeplinks/", tags=["deeplinks"], response_model=List[schemas.Deeplink])
async def list_deeplinks(x_jwt_payload: str = Header(None)):
    payload = get_jwt_payload(x_jwt_payload)
    return list(list_deeplinks_use_case(user_id=payload["user_id"]))
