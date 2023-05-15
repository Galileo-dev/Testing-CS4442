from datetime import timedelta
from firebase_admin import credentials, firestore, initialize_app

from Backend.booking import Booking

"""
To Do
--------
1. Get bookings
    -> return a list of all bookings on the db
2. Add booking
    -> add booking to db
"""


class Database:
    # cred = credentials.ApplicationDefault()

    def __init__(self):
        self.db = firestore.client()

    def getFirstRoom(self):
        rooms_ref = self.db.collection("rooms")
        rooms = rooms_ref.stream()
        room = next(rooms)
        return room.to_dict()["displayName"]

    def getRooms(self):
        rooms_ref = self.db.collection("rooms")
        rooms = rooms_ref.get()
        return [{"id": doc.id, **doc.to_dict()} for doc in rooms]

    def getFirstUser(self):
        users_ref = self.db.collection("users")
        users = users_ref.stream()
        user = next(users)
        return user.to_dict()["displayName"]

    def getNameFromUID(self, uid: str) -> dict | None:
        users_ref = self.db.collection("users")
        users = users_ref.stream()
        for user in users:
            if user.id == uid:
                return user.to_dict()
        return None

    def addBooking(self, booking: Booking):
        entry = {
            "start_time": booking.date_time,
            "end_time": booking.date_time + timedelta(hours=1),
            "uid": booking.uid,
        }
        bookings_ref = (
            self.db.collection("rooms").document(booking.room_id).collection("bookings")
        )
        update_time, ref = bookings_ref.add(entry)
        return ref.id

    def getBookings(self, room_id: str):
        bookings_ref = (
            self.db.collection("rooms").document(room_id).collection("bookings")
        )
        bookings_stream = bookings_ref.stream()
        bookings = []
        for booking in bookings_stream:
            booking_dict = booking.to_dict()
            new_booking = Booking(
                id=booking.id,
                room_id=room_id,
                uid=booking_dict["uid"],
                date_time=booking_dict["start_time"],
            )
            bookings.append(new_booking)
        return bookings

    def cancelBooking(self, room_id: str, booking_id: str):
        bookings_ref = (
            self.db.collection("rooms").document(room_id).collection("bookings")
        )
        try:
            bookings_ref.document(booking_id).delete()
            return "success"
        except firestore.NotFound:
            return "not found"

    # At the moment assuming that all bookings are 1 hr long. If we choose to
    # allow for more flexibility this must be changed
    def checkAvailable(self, booking: Booking):
        if booking == None:
            return False

        db_bookings = self.getBookings(booking.room_id)
        available = True
        for db_booking in db_bookings:
            # print("bid: " + booking.id)
            if booking.check_overlap(db_booking):
                available = False

        return available
