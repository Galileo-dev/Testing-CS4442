import pytest
from reservation import Reservation
from database import Database

def test_basic_functionality_rooms():
    database = Database
    assert isinstance(database.getFirstRoom(database), str)
    
def test_basic_functionality_users():
    database = Database
    assert isinstance(database.getFirstUser(database), str)
    
def test_get_name_from_uid():
    database = Database
    assert database.getNameFromUID(database, "KlhITEDxj5akF0cK7cymJmmonC93")["displayName"] == "Dara Newsome"
    
def test_get_reservations():
    database = Database
    reservations = database.getReservations()
    if reservations != []:
        assert isinstance(reservations[0], Reservation)
    
def test_add_reservation():
    database = Database
    new_reservation = Reservation(uid="KlhITEDxj5akF0cK7cymJmmonC93", room="Conference Room", unparsed_date_time=None, date_time=None, date_time_str="24-06 13:47")
    rid = database.addReservation(new_reservation)
    reservations = database.getReservations()
    exists = False
    for reservation in reservations:
        if reservation.id == rid:
            exists = True
    assert exists
    
    
