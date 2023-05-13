import pytest
from booking import Booking
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
    
def test_get_bookings():
    database = Database
    bookings = database.getBookings(database, 'conferenceroom')
    if bookings != []:
        assert isinstance(bookings[0], Booking)
    
def test_add_booking():
    database = Database
    new_booking = Booking(uid="KlhITEDxj5akF0cK7cymJmmonC93", room_id="conferenceroom", unparsed_date_time=None, date_time=None, date_time_str="24-06 13:47")
    new_booking.format()
    bid = database.addBooking(database, booking=new_booking)
    # print("bid: " + bid)
    bookings = database.getBookings(database, new_booking.room_id)
    exists = False
    for booking in bookings:
        print("bid: " + booking.id)
        if booking.id == bid:
            exists = True
    assert exists
    
    # Delete document to reset testing environment
    database.cancelBooking(database, new_booking.room_id, bid)
    
def test_cancel_booking():
    # Add new booking, check that it exists. Delete booking, check that it doesn't exist.
    database = Database
    new_booking = Booking(uid="KlhITEDxj5akF0cK7cymJmmonC93", room_id="conferenceroom", unparsed_date_time=None, date_time=None, date_time_str="24-06 13:47")
    new_booking.format()
    bid = database.addBooking(database, booking=new_booking)
    # print("bid: " + rid)
    bookings = database.getBookings(database, 'conferenceroom')
    exists = False
    for booking in bookings:
        # print("bid: " + booking.id)
        if booking.id == bid:
            exists = True
    assert exists
    
    database.cancelBooking(database, new_booking.room_id, bid)
    bookings = database.getBookings(database, 'conferenceroom')
    exists = False
    for booking in bookings:
        # print("bid: " + booking.id)
        if booking.id == bid:
            exists = True
    assert (not exists)
    
def test_check_is_time_available_false():
    database = Database
    booking1 = Booking(uid="KlhITEDxj5akF0cK7cymJmmonC93", room_id="conferenceroom", unparsed_date_time=None, date_time=None, date_time_str="11-05 16:21", length_in_mins=25)
    booking1.format()
    b1id = database.addBooking(database, booking1)
    booking2 = Booking(uid="KlhITEDxj5akF0cK7cymJmmonC93", room_id="conferenceroom", unparsed_date_time=None, date_time=None, date_time_str="11-05 16:41", length_in_mins=30)
    booking2.format()
    assert (not database.checkAvailable(database, booking2))
    database.cancelBooking(database, booking1.room_id, b1id)
    
def test_check_is_time_available_true():
    database = Database
    booking1 = Booking(uid="KlhITEDxj5akF0cK7cymJmmonC93", room_id="conferenceroom", unparsed_date_time=None, date_time=None, date_time_str="11-05 10:21", length_in_mins=10)
    booking1.format()
    b1id = database.addBooking(database, booking1)
    booking2 = Booking(uid="KlhITEDxj5akF0cK7cymJmmonC93", room_id="conferenceroom", unparsed_date_time=None, date_time=None, date_time_str="11-05 10:41", length_in_mins=30)
    booking2.format()
    assert (not database.checkAvailable(database, booking2))
    database.cancelBooking(database, booking1.room_id, b1id)
    
    
