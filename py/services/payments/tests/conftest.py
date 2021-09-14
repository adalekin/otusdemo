import asyncio
import warnings

import pytest
from aiokafka.producer import AIOKafkaProducer
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from manage import downgrade, upgrade
from payments import schemas
from payments.dependencies import get_db


# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="session", autouse=True)
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    upgrade()
    yield
    downgrade()


@pytest.fixture(scope="session")
def db():
    yield from get_db()


@pytest.fixture
async def client(mocker):
    for class_method in ("start", "send", "stop"):
        future = asyncio.Future()
        future.set_result(None)

        mocker.patch.object(AIOKafkaProducer, class_method, return_value=future)

    from payments.main import app

    async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(app):
        yield client


@pytest.fixture
async def payment(client):
    response = await client.post(
        "/payments/",
        json={"order_id": 1, "amount": 5000, "currency": "USD"},
    )
    assert response.status_code == 201
    return schemas.Payment(**response.json())
