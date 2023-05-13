from datetime import datetime, timedelta, timezone
from typing import Optional
from pydantic import BaseModel

from gptparser import GPTParser


class Booking(BaseModel):
    id: Optional[str] = None
    room_id: str
    uid: Optional[str] = None
    unparsed_date_time: Optional[str] = None
    date_time_str: Optional[str] = None
    date_time: Optional[datetime] = None
    length_in_mins: Optional[int] = 60

    def parse(self):
        self.date_time_str = GPTParser.datetime_parser(self.unparsed_date_time)

    def format(self):
        self.date_time = datetime.strptime(self.date_time_str, '%d-%m %H:%M')
        self.date_time = datetime(year=2023, month=self.date_time.month, day=self.date_time.day, hour=self.date_time.hour, minute=self.date_time.minute, tzinfo=timezone.utc)
        
    def check_overlap(self, comparand: 'Booking'):
        start1 = self.date_time
        end1 = self.date_time + timedelta(minutes=self.length_in_mins)
        
        start2 = comparand.date_time
        end2 = comparand.date_time + timedelta(minutes=comparand.length_in_mins)
        
        if start1 >= end2 or start2 >= end1:
            return False
        else:
            return True