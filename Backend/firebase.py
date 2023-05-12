from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("../book_me_service_account_keys.json")
app = initialize_app(cred)

def get_firebase_app():
    return app
