import pytest
from Backend.booking import Booking


@pytest.mark.parametrize(
    "date_time_str, expected_month, expected_day, expected_hour, expected_minute",
    [
        ("11-05 12:36", 5, 11, 12, 36),
        ("01-15 05:45", 1, 15, 5, 45),
        ("06-25 23:59", 6, 25, 23, 59),
    ],
)
def test_booking_class_formatter(firebase_app, date_time_str, expected_month, expected_day, expected_hour, expected_minute):
    booking = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str=date_time_str,
    )
    booking.format()
    assert booking.date_time.month == expected_month
    assert booking.date_time.day == expected_day
    assert booking.date_time.hour == expected_hour
    assert booking.date_time.minute == expected_minute


def test_check_overlap_simple_true(firebase_app):
    booking1 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 12:00",
        length_in_mins=45,
    )
    booking1.format()
    booking2 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 12:15",
        length_in_mins=30,
    )
    booking2.format()
    assert booking1.check_overlap(booking2)


def test_check_overlap_simple_false(firebase_app):
    booking1 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 12:00",
        length_in_mins=10,
    )
    booking1.format()
    booking2 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 12:15",
        length_in_mins=30,
    )
    booking2.format()
    assert not booking1.check_overlap(booking)


def test_check_overlap_border_true(firebase_app):
    booking1 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 10:15",
        length_in_mins=16,
    )
    booking1.format()
    booking2 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 10:30",
        length_in_mins=30,
    )
    booking2.format()
    assert booking1.check_overlap(booking2)


def test_check_overlap_border_false(firebase_app):
    booking1 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 16:21",
        length_in_mins=20,
    )
    booking1.format()
    booking2 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 16:41",
        length_in_mins=30,
    )
    booking2.format()
    assert not booking1.check_overlap(booking2)

def test_booking_at_midnight(firebase_app):
    booking = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 00:00",
        length_in_mins=60,
    )
    booking.format()
    assert booking.date_time.hour == 0
    assert booking.date_time.minute == 0


def test_booking_with_no_length(firebase_app):
    booking = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 12:00",
        length_in_mins=None,
    )
    booking.format()
    assert booking.length_in_mins == 0


def test_booking_lasting_full_day(firebase_app):
    booking = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 00:00",
        length_in_mins=1440, # 24 hours
    )
    booking.format()
    assert booking.length_in_mins == 1440
    assert booking.date_time.hour == 0
    assert booking.date_time.minute == 0


def test_check_overlap_start_of_day_true(firebase_app):
    booking1 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-05 23:30",
        length_in_mins=60,
    )
    booking1.format()
    booking2 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="11-06 00:00",
        length_in_mins=30,
    )
    booking2.format()
    assert booking1.check_overlap(booking2)


def test_check_overlap_end_of_day_true(firebase_app):
    booking1 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="05-15 23:45",
        length_in_mins=15,
    )
    booking1.format()
    booking2 = Booking(
        uid="JrDdit1L3qBhXcnWj9uU",
        room_id="Y7xMXElgNqqxAiQOCQ3y",
        unparsed_date_time=None,
        date_time=None,
        date_time_str="05-15 23:59",
        length_in_mins=120,
    )
    booking2.format()
    assert booking1.check_overlap(booking2)


    

def test_invalid_date_time_string(firebase_app):
    with pytest.raises(ValueError):
        Booking(
            uid="JrDdit1L3qBhXcnWj9uU",
            room_id="Y7xMXElgNqqxAiQOCQ3y",
            unparsed_date_time=None,
            date_time=None,
            date_time_str="invalid_date_time_string",
        )


def test_invalid_length(firebase_app):
    with pytest.raises(ValueError):
        Booking(
            uid="JrDdit1L3qBhXcnWj9uU",
            room_id="Y7xMXElgNqqxAiQOCQ3y",
            unparsed_date_time=None,
            date_time=None,
            date_time_str="11-05 12:00",
            length_in_mins=-10,
        )
