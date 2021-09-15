import pytest
from events.use_cases.id import encode_id_use_case


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "event_data",
    [
        {"t": "pageview", "tid": encode_id_use_case(123), "cid": "123"},
        {"t": "event", "tid": encode_id_use_case(123), "cid": "123", "ec": "revenue", "ev": 100},
    ],
)
async def test_events_create(client, event_data):
    response = await client.post("/events/", json=event_data)
    assert response.status_code == 201
