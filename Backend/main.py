from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from firebase_admin import credentials, initialize_app
from firebase import Firebase


Firebase.get_firebase_app()
from routers import booking, users, auth
from dependencies import get_query_token, get_token_header


app = FastAPI(dependencies=[])


allow_all = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all,
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(booking.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
