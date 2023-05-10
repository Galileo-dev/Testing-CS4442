from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dependencies import get_query_token, get_token_header
<<<<<<< HEAD
from routers import users, auth


app = FastAPI(dependencies=[])
allow_all = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all
)


app.include_router(users.router)
app.include_router(auth.router)
=======
from routers import add_reservation

#app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(add_reservation.router)
>>>>>>> f2954af (started on supabase implementation)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
