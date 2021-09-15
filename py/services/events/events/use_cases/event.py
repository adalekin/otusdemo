import datetime
import json

from schemas.event import EventFired

from events import models, schemas
from events.database import db
from events.exceptions import PartnerNotFound
from events.kafka import producer
from events.use_cases.id import decode_id_use_case


async def create_event_use_case(create_event: schemas.CreateEvent):
    event = schemas.Event(created_at=datetime.datetime.utcnow(), **create_event.dict())

    partner_id = decode_id_use_case(event.tid)

    if not partner_id:
        raise PartnerNotFound()
    partner_id = partner_id[0]

    event_orm = models.Event.create(partner_id=partner_id, **event.dict())
    event_fired = EventFired(partner_id=partner_id, **event.dict())

    await producer.send("event-fired", json.dumps(event_fired.json()).encode("utf-8"))

    return schemas.Event.from_orm(event_orm)
