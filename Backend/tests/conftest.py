from app.firebase import Firebase
import pytest
import os


@pytest.fixture(scope="session")
def firebase_app():
    os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"
    os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = "localhost:9099"
    os.environ["FIREBASE_DATABASE_EMULATOR_HOST"] = "localhost:9000"
    os.environ["FIREBASE_FUNCTIONS_EMULATOR_HOST"] = "localhost:5001"
    os.environ["FIREBASE_STORAGE_EMULATOR_HOST"] = "localhost:9199"

    return Firebase.get_firebase_app()
