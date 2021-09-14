import pytest


@pytest.mark.asyncio()
async def test_products_list(client):
    response = await client.get("/products/")
    assert response.status_code == 200
    assert response.json()
