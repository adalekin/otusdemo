import warnings

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from manage import downgrade, upgrade
from products import models, schemas
from products.dependencies import get_db
from products.main import app


# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="session", autouse=True)
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    upgrade()
    yield
    downgrade()


@pytest.fixture(scope="session")
def db():
    yield from get_db()


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(app):
        yield client


@pytest.fixture
async def product(db):
    return schemas.Product.from_orm(db.query(models.Product).first())


@pytest.fixture
async def reservation(client, product):
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
    return schemas.Reservation(**response.json())
