from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

import sys
from routers.auth import get_user_token
# from routers.auth import get_user_token
sys.path.append('..')
from gptparser import GPTParser

router = APIRouter()

class Reservation(BaseModel):
    # name: str
    room: str
    unparsed_date_time: Optional[str] = None
    date_time: Optional[date_time] = None
    date_time_str: Optional[str] = None

    def parse(self):
        self.date_time_str = GPTParser.datetime_parser(self.unparsed_date_time)

    def format(self):
        self.date_time = datetime.strptime(self.date_time_str, '%d-%m %H:%M')
        self.date_time = datetime(year=2023, month=self.date_time.month, day=self.date_time.day, hour=self.date_time.hour, minute=self.date_time.minute)

@router.post("/add_reservation/")
async def add_reservation(reservation: Reservation, user=Depends(get_user_token)):
            
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
