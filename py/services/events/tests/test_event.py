import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize("event_data", [{"t": "pageview", "partner_id": "123", "cid": "123"}])
async def test_events_create(client, event_data):
    response = await client.post("/events/", json=event_data)
    assert response.status_code == 201
