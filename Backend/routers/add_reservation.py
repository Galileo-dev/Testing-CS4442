from fastapi import APIRouter, Depends

from reservation import Reservation
from routers.auth import get_user_token

router = APIRouter()

@router.post("/add_reservation/")
async def add_reservation(reservation: Reservation, user=Depends(get_user_token)):
    reservation.uid = user['uid']
    if reservation.unparsed_date_time is str:
        reservation.parse()
    reservation.format()
    return { "user id": user["uid"],"room": reservation.room, "date_time": reservation.date_time.isoformat() }

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
