from orders import settings


def test_orders_create(client, requests_mock):
    requests_mock.post(settings.AFFO_URL + "/events/", status_code=201)

    response = client.post(
        "/orders/",
        json={"items": [{"product_id": 1, "quantity": 1}, {"product_id": 2, "quantity": 2}]},
    )

    assert response.status_code == 201


def test_orders_create_via_affo(client, requests_mock):
    requests_mock.post(settings.AFFO_URL + "/events/", status_code=201)

    response = client.post(
        "/orders/",
        json={"items": [{"product_id": 1, "quantity": 1}, {"product_id": 2, "quantity": 2}], "tid": "1", "cid": "1"},
    )

    assert response.status_code == 201
