from datetime import datetime, timedelta, timezone
from typing import Optional
from pydantic import BaseModel

from app.gptparser import GPTParser


class Booking(BaseModel):
    id: Optional[str] = None
    room_id: str
    uid: Optional[str] = None
    unparsed_date_time: Optional[str] = None
    date_time_str: Optional[str] = None
    date_time: Optional[datetime] = None
    length_in_mins: int = 60

    def parse(self):
        if not isinstance(self.unparsed_date_time, str):
            assert False, "unparsed_date_time is not a string"
        gpt_parser = GPTParser()
        self.date_time_str = gpt_parser.datetime_parser(
            string=str(self.unparsed_date_time)
        )

    def format(self):
        if self.length_in_mins < 1:
            raise ValueError("length_in_mins cannot be negative or zero")

        if not isinstance(self.date_time_str, str):
            assert False, "date_time_str is not a string"

        self.date_time = datetime.strptime(str(self.date_time_str), "%d-%m %H:%M")
        self.date_time = datetime(
            year=2023,
            month=self.date_time.month,
            day=self.date_time.day,
            hour=self.date_time.hour,
            minute=self.date_time.minute,
            tzinfo=timezone.utc,
        )

    def check_overlap(self, comparand: "Booking"):
        # if none raise an exception
        if self.date_time is None:
            raise ValueError("self.date_time cannot be None")
        start1 = self.date_time

        if self.length_in_mins is None:
            raise ValueError("date_time cannot be None")
        length_in_mins = self.length_in_mins

        end1 = self.date_time + timedelta(minutes=length_in_mins)

        if comparand.date_time is None:
            raise ValueError("comparand.date_time cannot be None")
        start2 = comparand.date_time

        end2 = comparand.date_time + timedelta(minutes=comparand.length_in_mins or 0)

        if start1 >= end2 or start2 >= end1:
            return False
        else:
            return True
