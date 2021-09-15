import base64
import json

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

import manage


@pytest.fixture()
async def client(mocker):
    from stats.main import app

    async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(app):
        yield client


@pytest.fixture()
def user_jwt_payload():
    return base64.b64encode(json.dumps({"user_id": 1}).encode("utf-8"))
