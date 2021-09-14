from fastapi import APIRouter

router = APIRouter()


@router.get("/liveness/", tags=["probe"])
async def liveness():
    return {}
