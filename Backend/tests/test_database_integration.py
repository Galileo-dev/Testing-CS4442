import pytest
from app.booking import Booking
from app.database import Database


def test_basic_functionality_rooms(firebase_app):
    database = Database()

    assert isinstance(database.getFirstRoom(), str)


def test_basic_functionality_users(firebase_app):
    database = Database()
    assert isinstance(database.getFirstUser(), str)


def test_get_name_from_uid(firebase_app):
    database = Database()
    user = database.getNameFromUID("JrDdit1L3qBhXcnWj9uU")
    assert user != None and user.get("displayName") == "Ada Lovelace"


def test_get_bookings(firebase_app):
    database = Database()
    bookings = database.getBookings("Y7xMXElgNqqxAiQOCQ3y")
    if bookings != []:
        assert isinstance(bookings[0], Booking)


def test_add_booking(firebase_app):
    database = Database()
    new_booking = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="24-06 13:47",
    )
    new_booking.format()
    bid = database.addBooking(booking=new_booking)
    # print("bid: " + bid)
    bookings = database.getBookings(new_booking.room_id)
    exists = False
    for booking in bookings:
        print("bid: " + booking.id)
        if booking.id == bid:
            exists = True
    assert exists

    # Delete document to reset testing environment
    database.cancelBooking(new_booking.room_id, bid)


def test_cancel_booking(firebase_app):
    # Add new booking, check that it exists. Delete booking, check that it doesn't exist.
    database = Database()
    new_booking = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="24-06 13:47",
    )
    new_booking.format()
    bid = database.addBooking(booking=new_booking)
    # print("bid: " + rid)
    bookings = database.getBookings("Y7xMXElgNqqxAiQOCQ3y")
    exists = False
    for booking in bookings:
        # print("bid: " + booking.id)
        if booking.id == bid:
            exists = True
    assert exists

    database.cancelBooking(new_booking.room_id, bid)
    bookings = database.getBookings("Y7xMXElgNqqxAiQOCQ3y")
    exists = False
    for booking in bookings:
        # print("bid: " + booking.id)
        if booking.id == bid:
            exists = True
    assert not exists


def test_check_is_time_available_false(firebase_app):
    database = Database()
    booking1 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 16:21",
        length_in_mins=25,
    )
    booking1.format()
    b1id = database.addBooking(booking1)
    booking2 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 16:41",
        length_in_mins=30,
    )
    booking2.format()
    assert not database.checkAvailable(booking2)
    database.cancelBooking(booking1.room_id, b1id)


def test_check_is_time_available_true(firebase_app):
    database = Database()
    booking1 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 10:21",
        length_in_mins=10,
    )
    booking1.format()
    b1id = database.addBooking(booking1)
    booking2 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 10:41",
        length_in_mins=30,
    )
    booking2.format()
    assert not database.checkAvailable(booking2)
    database.cancelBooking(booking1.room_id, b1id)
