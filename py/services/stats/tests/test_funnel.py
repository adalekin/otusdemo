import pytest


@pytest.mark.asyncio
async def test_funnel_create(client, user_jwt_payload):
    response = await client.get("/funnel/daily/", headers={"X-JWT-Payload": user_jwt_payload})
    assert response.status_code == 200
