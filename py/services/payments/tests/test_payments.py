import pytest


@pytest.mark.asyncio
async def test_payments_create(client):
    response = await client.post(
        "/payments/",
        json={"order_id": 1, "amount": 5000, "currency": "USD"},
    )
    assert response.status_code == 201

    payment_data = response.json()
    assert payment_data["status"] == "created"


@pytest.mark.asyncio
async def test_payments_confirm(client, payment):
    response = await client.post(f"/payments/{payment.id}/confirm/")
    assert response.status_code == 200

    payment_data = response.json()
    assert payment_data["status"] == "confirmed"
