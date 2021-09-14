import base64
import json
import uuid

import pytest
from hamcrest import assert_that
from pytest_toolbelt import matchers

from users import settings
from users.application import create_app
from users.extensions import db as db_

TEST_DATABASE_URI = f"sqlite://"


@pytest.fixture(scope="session", autouse=True)
def app(request):
    settings_override = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": TEST_DATABASE_URI, "CACHE_TYPE": "simple"}
    app = create_app(settings_override)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="session", autouse=True)
def db(app, request):
    db_.app = app
    db_.create_all()

    return db_


@pytest.fixture(scope="function")
def session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope="session")
def client(app, db):
    return app.test_client()


@pytest.fixture()
def user_access_token():
    return "123"


@pytest.fixture()
def account_id():
    return "123"


@pytest.fixture()
def user(client, requests_mock, user_access_token, account_id):
    requests_mock.post(settings.AUTH_URL + "/jwt/encode/", json={"access_token": user_access_token})
    requests_mock.post(settings.BILLING_URL + "/accounts/", json={"id": account_id})

    password = "1234567890"

    response = client.post(
        "/register/",
        json={
            "email": f"test-{uuid.uuid4()}@example.com",
            "first_name": "晓鹏",
            "last_name": "郑",
            "password": password,
        },
    )

    assert_that(response, matchers.has_status(201))

    return (response.json, password)


@pytest.fixture()
def user_jwt_payload(user):
    user, _ = user

    return base64.b64encode(json.dumps({"user_id": user["id"]}).encode("utf-8"))
