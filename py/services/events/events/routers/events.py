from fastapi import APIRouter

from events import schemas
from events.use_cases.event import create_event_use_case

router = APIRouter()


@router.post("/events/", tags=["events"], status_code=201, response_model=schemas.Event)
async def create_event(create_event: schemas.CreateEvent):
    return await create_event_use_case(create_event)
