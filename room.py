class Hotel:
    def __init__(self, destination, the_residences, offer, experiences,event_meeting):
        self.__destination = destination
        self.__the_residences = the_residences
        self.__offer = offer
        self.__experiences =  experiences
        self.__event_meeting = event_meeting

class Roomcatalog:
    def __init__(self, room_list):
        self.__room_list = []

class Room:
    def __init__(self, room_name, room_area, room_description, number_bathroom, number_bedroom, room_capacity, bedtype, tv_usb, jacuzzi, dvdplayer, fridge, air_conditioner):
        self._room_name = room_name
        self._room_area = room_area
        self._room_description = room_description
        self._number_of_bathroom = number_bathroom
        self._number_of_bedroom = number_bedroom
        self._room_capacity = room_capacity
        self._bedtype = bedtype
        self._tv_and_ubc = tv_usb
        self._jacuzzi = jacuzzi
        self._DVDplayer = dvdplayer
        self._fridge = fridge
        self._air_conditioner = air_conditioner


class ReserveRoom:
    def __init__(self, room_list):
        self.__room_list = []




class Payment:
    def __inti__(self, credit_card, status):
        self.__credit_card = credit_card
        self.__status = status


class Creditcard:
    def __inti__(self, card_number, cardholder_name, expiry_date, cvv, country, bank, email):
        self.__card_number = card_number
        self.__cardholder_name = cardholder_name
        self.__expiry_date = expiry_date
        self.__cvv = cvv
        self.__country = country
        self.__bank = bank
        self.__email = email


class Promotion:
    def __init__(self, code):
        self.__code = code


class Booking:
    def __init__(self, date_in, date_out, promotion_code, status):
        self.__date_in = date_in
        self.__date_out = date_out
        self.__country = promotion_code
        self.__status = status


class BookingHistory:
    def __init__(self, booking_detail):
        self.__booking_detail = booking_detail


##ENUM

class Paymentstatus(Enum):
    COMPLETE, INCOMPLETE = 1,2

class Bookingstatus(Enum):
    PENDING, COMFIRM, CANCEL = 1,2,3

class Roomstatus(Enum):
    AVAILBLE, FULL, ON_REQUEST = 1,2,3
        

##person

class Accout:
    def __init__(self, email, password):
        self._email = email
        self._password = password

class User:
    def __inti__(self, title, name, surname, address):
        self.__title = title
        self.__name = name
        self.__surname = surname
        self.__address = address

class Guest:
    def __init__(self):

class Admin:
    def __init__(self):
