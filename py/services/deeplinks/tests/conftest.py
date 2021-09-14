import asyncio
import base64
import json

import pytest
from httpx import AsyncClient

import manage  # noqa
from deeplinks import schemas
from deeplinks.http import client as events_client
from deeplinks.use_cases.deeplink import create_deeplink_use_case


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def close_http_client():
    yield None
    await events_client.aclose()


@pytest.fixture()
async def client():
    from deeplinks.main import app

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture()
def user_jwt_payload():
    return base64.b64encode(json.dumps({"user_id": 1}).encode("utf-8"))


@pytest.fixture()
def deeplink():
    return create_deeplink_use_case(
        user_id=1, create_deeplink=schemas.CreateDeeplink(user_id=1, url="http://example.com", cn="test", cs="test")
    )
