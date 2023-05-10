import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def test_firestore():
    # Initialize the Firebase SDK
    cred = credentials.Certificate("../book_me_service_account_keys.json")
    firebase_admin.initialize_app(cred)

    # Add some data to Firestore
    db = firestore.client()
    doc_ref = db.collection("users").document("alovelace")
    doc_ref.set({
        "first": "Ada",
        "last": "Lovelace",
        "born": 1815
    })

    # Retrieve the data from Firestore
    doc = doc_ref.get()
    assert doc.to_dict() == {
        "first": "Ada",
        "last": "Lovelace",
        "born": 1815
    }
