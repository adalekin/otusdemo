import pytest
import respx
from httpx import Response

from deeplinks import settings


@pytest.mark.asyncio
@pytest.mark.parametrize("id", ["", "123", "test", "ава"])
async def test_deeplinks_redirect_not_found(client, id):
    response = await client.get(f"/{id}", allow_redirects=False)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_deeplinks_redirect(client, deeplink):
    respx.post(f"{settings.EVENTS_URL}/events/").mock(return_value=Response(200))

    response = await client.get(f"/{deeplink.id}", allow_redirects=False)
    assert response.status_code == 301

@pytest.mark.asyncio
async def test_deeplinks_list(client, deeplink, user_jwt_payload):
    response = await client.get("/deeplinks/", headers={"X-JWT-Payload": user_jwt_payload})
    assert response.status_code == 200
    assert response.json()
