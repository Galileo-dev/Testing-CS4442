from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from gptparser import GPTParser


class Reservation(BaseModel):
    id: Optional[str] = None
    room: str
    uid: Optional[str] = None
    unparsed_date_time: Optional[str] = None
    date_time: Optional[date_time] = None
    date_time_str: Optional[str] = None

    def parse(self):
        self.date_time_str = GPTParser.datetime_parser(self.unparsed_date_time)

    def format(self):
        self.date_time = datetime.strptime(self.date_time_str, '%d-%m %H:%M')
        self.date_time = datetime(year=2023, month=self.date_time.month, day=self.date_time.day, hour=self.date_time.hour, minute=self.date_time.minute)