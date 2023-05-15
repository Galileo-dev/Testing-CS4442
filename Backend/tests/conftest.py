import requests
from app import routers
from app.firebase import Firebase
import pytest
import os

from fastapi import status
from fastapi.testclient import TestClient
from firebase_admin import auth, initialize_app, credentials
from app.main import app


@pytest.fixture(scope="session")
def firebase_app():
    os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"
    os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "localhost:9099"
    os.environ["FIREBASE_DATABASE_EMULATOR_HOST"] = "localhost:9000"
    os.environ["FIREBASE_FUNCTIONS_EMULATOR_HOST"] = "localhost:5001"
    os.environ["FIREBASE_STORAGE_EMULATOR_HOST"] = "localhost:9199"

    return Firebase.get_firebase_app()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def firebase_auth(firebase_app):
    return auth


@pytest.fixture
def firebase_user(firebase_auth):
    try:
        user = firebase_auth.get_user("test_user")
    except auth.UserNotFoundError:
        user = firebase_auth.create_user(uid="test_user")
    return user


@pytest.fixture
def firebase_test_token(firebase_user):
    custom_token = auth.create_custom_token(firebase_user.uid).decode("utf-8")

    url = "http://localhost:9099/identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=hello"

    payload = {"token": custom_token, "returnSecureToken": True}

    response = requests.post(url, json=payload)

    if response.ok:
        id_token = response.json()["idToken"]
    else:
        error_message = response.json()["error"]["message"]
        # show in test
        assert False, error_message

    return id_token


def test_hello_user(client, firebase_user, firebase_test_token):
    response = client.get(
        "/api/user_token", headers={"Authorization": f"Bearer {firebase_test_token}"}
    )

    # response = client.get('/api/user_token', headers={'Authorization': f'Bearer {custom_token}'})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Hello, user", "uid": f"{firebase_user.uid}"}