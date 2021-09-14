import asyncio

import pytest
from aiokafka.producer import AIOKafkaProducer
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

import manage
from statistics import schemas
from statistics.use_cases.event import create_event_use_case


@pytest.fixture()
async def client(mocker):
    for class_method in ("start", "send", "stop"):
        future = asyncio.Future()
        future.set_result(None)

        mocker.patch.object(AIOKafkaProducer, class_method, return_value=future)

    from statistics.main import app

    async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(app):
        yield client


@pytest.fixture()
def event():
    return create_event_use_case(schemas.CreateEvent(user_id=1, url="http://example.com", cn="test", cs="test"))
