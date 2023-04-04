import datetime
class Booking:
    def __init__(self, date_in, date_out, amount):
        self._date_in = date_in
        self._date_out = date_out
        self._amount = amount
        amount = date_out - date_in
        
