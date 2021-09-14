import datetime

from schemas.event import EventFired

from events import models, schemas
from events.kafka import producer


async def create_event_use_case(create_event: schemas.CreateEvent):
    event = schemas.Event(created_at=datetime.datetime.utcnow(), **create_event.dict())
    event_orm = models.Event.create(**event.dict())

    event_fired = EventFired(**event.dict())
    await producer.send("event-fired", event_fired.json())

    return schemas.Event.from_orm(event_orm)
