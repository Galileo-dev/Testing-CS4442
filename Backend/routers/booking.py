import datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from Backend.booking import Booking
from Backend.database import Database
from Backend.routers.auth import get_user_token
from typing import Optional
from datetime import datetime

router = APIRouter()


@router.post("/add_booking/")
async def add_booking(booking: Booking, user=Depends(get_user_token)):
    booking.uid = user["uid"]
    if booking.unparsed_date_time is str:
        booking.parse()
    booking.format()

    database = Database()
    available = database.checkAvailable(booking)
    if available:
        id = database.addBooking(booking)
        return {
            "result": "success",
            "message": f"This time is available and a booking with id {id} has been added to the database",
        }
    else:
        return {
            "result": "failed",
            "message": "The chosen time/room is not available, please choose another",
        }


@router.delete("/cancel_booking/{room_id}/{booking_id}")
def delete_booking(room_id, booking_id):
    database = Database
    response = database.cancelBooking(database, room_id=room_id, booking_id=booking_id)
    if response == "success":
        return {
            "result": "success",
            "message": f"Booking with id {booking_id} has been deleted",
        }
    if response == "not found":
        return {
            "result": "failed",
            "message": f"Booking with id {booking_id} does not exist",
        }


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
