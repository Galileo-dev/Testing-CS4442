# import pytest
from fastapi import status
# from fastapi.testclient import TestClient
# from firebase_admin import auth, initialize_app, credentials
# import requests
# from app.routers.auth import router


# import os


# @pytest.fixture
# def client():
#     return TestClient(router)


# @pytest.fixture
# def firebase_auth(firebase_app):
#     return auth


# @pytest.fixture
# def firebase_user(firebase_auth):
#     try:
#         user = firebase_auth.get_user("test_user")
#     except auth.UserNotFoundError:
#         user = firebase_auth.create_user(uid="test_user")
#     return user


# @pytest.fixture
# def firebase_test_token(firebase_user):
#     custom_token = auth.create_custom_token(firebase_user.uid).decode("utf-8")

#     url = "http://localhost:9099/identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=hello"

#     payload = {"token": custom_token, "returnSecureToken": True}

#     response = requests.post(url, json=payload)

#     if response.ok:
#         id_token = response.json()["idToken"]
#     else:
#         error_message = response.json()["error"]["message"]
#         # show in test
#         assert False, error_message

#     return id_token


def test_hello_user(client, firebase_user, firebase_test_token):
    response = client.get(
        "/api/user_token", headers={"Authorization": f"Bearer {firebase_test_token}"}
    )

    # response = client.get('/api/user_token', headers={'Authorization': f'Bearer {custom_token}'})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Hello, user", "uid": f"{firebase_user.uid}"}
    
    
# def test_add_reservation(client, firebase_user, firebase_test_token):
#     response = client.get(
#         "/add_reservation", headers={"Authorization": f"Bearer {firebase_test_token}"}
#     )

#     # response = client.get('/api/user_token', headers={'Authorization': f'Bearer {custom_token}'})
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {"msg": "Hello, user", "uid": f"{firebase_user.uid}"}