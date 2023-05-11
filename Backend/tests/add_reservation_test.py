import pytest
from routers.add_reservation import Reservation
from datetime import datetime

# parameters = [
#     ("The eleventh of november at ten o'clock", "11-11 10:00"),
#     ("The 26th of aug at 11.15", "26-08 11:15"),
#     ("11th of Nov at 1 o'clock", "11-11 01:00"),
#     ("The thirteenth of april at one am", "13-04 01:00"),
#     ("The 13th of dec at one pm", "13-12 13:00")
# ]

# @pytest.mark.parametrize("param, expected_result", parameters)
# def test_my_function(param, expected_result):
# @pytest.fixture
def test_reservation_class_formatter(): 
    reservation = Reservation(name="Conor", room="Conference Room", unparsed_date_time=None, date_time=None, date_time_str="11-05 12:36")
    reservation.format()
    assert reservation.date_time.month == 5
    assert reservation.date_time.day == 11
    assert reservation.date_time.hour == 12
    assert reservation.date_time.minute == 36
