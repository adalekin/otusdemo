import pytest


@pytest.mark.asyncio
async def test_reservations_create(client, product):
    response = await client.post(
        "/reservations/",
        json={
            "order_id": 1,
            "product_id": product.id,
            "price": product.price,
            "price_currency": product.price_currency,
            "quantity": 2,
        },
    )
    assert response.status_code == 201

    reservation_data = response.json()
    assert reservation_data["status"] == "created"


@pytest.mark.asyncio
async def test_reservations_confirm(client, reservation):
    response = await client.post(f"/reservations/{reservation.id}/confirm/")
    assert response.status_code == 200

    reservation_data = response.json()
    assert reservation_data["status"] == "confirmed"
