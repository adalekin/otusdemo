import pytest


@pytest.mark.asyncio()
async def test_probe(client):
    response = await client.get("/liveness/")
    assert response.status_code == 200
