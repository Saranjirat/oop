import datetime
import uuid
from room import Room
class Booking:
    existng_booking_id= set()

    def __init__(self, start_time, end_time):
        self._start_time = start_time
        self._end_time = end_time
        self._amount = Room._room_amount 
        self._night = start_time - end_time
        self._price = self.night.days * self._amount
        self._details = {"name": None , "phone_num" : None, "email": None}
        self._paymentinfo = {"Metod" : None}
        self._booking_id = Booking.generate_booking_id()

    def generate_booking_id(cls):
        while True:
            booking_id = str(uuid.uuid4().hex)[:8]
            if booking_id not in cls.existing_booking_ids:
                cls.existing_booking_ids.add(booking_id)
                return booking_id
        
    
