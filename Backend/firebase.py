from firebase_admin import credentials, initialize_app
import os


class Firebase:
    _app = None

    @classmethod
    def get_firebase_app(cls):
        if cls._app is None:
            # get path to service account keys relative to this file
            path = os.path.join(
                os.path.dirname(__file__), "book_me_service_account_keys.json"
            )

            cred = credentials.Certificate(path)
            cls._app = initialize_app(cred)
        return cls._app
