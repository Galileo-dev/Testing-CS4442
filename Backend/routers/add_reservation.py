from fastapi import APIRouter
from pydantic import BaseModel
from enum import Enum
from datetime import datetime

import sys
sys.path.append('..')
from gptparser import GPTParser
from sbdb import SupabaseDB

router = APIRouter()

class Reservation(BaseModel):
    name: str
    room: str
    unparsed_date_time: str | None = None
    date_time: datetime | None = None
    date_time_str: str | None = None

    def parse(self):
        self.date_time_str = GPTParser.datetime_parser(self.unparsed_date_time)
        self.date_time =  datetime.strptime(, '%m-%d %H:%M')
        self.date_time_str = parsed_string

@router.post("/add_reservation/")
async def add_reservation(reservation: Reservation):
    reservation.parse()
    reservation.unparsed_date_time = None
    #reservation_dict = reservation.dict()
    #return { "name": reservation.name, "room": reservation.room, "month": reservation.date_time.month, "day": reservation.date_time.day, "hour": reservation.date_time.hour, "minute": reservation.date_time.minute }
    return { "name": reservation.name, "room": reservation.room, "date_time": reservation.date_time }

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
