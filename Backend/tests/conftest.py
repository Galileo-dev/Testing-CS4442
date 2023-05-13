from firebase_admin import credentials, initialize_app

cred = credentials.Certificate('./book_me_service_account_keys.json')
initialize_app(cred)
