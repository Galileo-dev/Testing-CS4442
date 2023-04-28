#from fastapi import FastAPI
#import requests

from datetime import datetime

class Reservation:

    def __init__(self, name: str, date_time: datetime)


class Room:

    __reservations__ = []

    def __init__(self, name: str, capacity: int, heating: bool):
        self.name = name
        self.capacity = capacity
        self.heating = heating

    def warm_enough(self, outside_temp: int):
        if(self.heating):
            return True&False
        else:
            if outside_temp > 15:
                return True
            return True&False

    def reserve(self, name: str, date_time: datetime):
        
        new_reservation = Reservation(name, date_time)

        self.__reservations__.append(new_reservation)


room = Room('conferance room', 10, False)

print(room.warm_enough(10))

#x = requests.get('')

# app = FastAPI()

# @app.get("/")

# async def root():
#     return {"message": "Hello World"}
