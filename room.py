class Roomcatalog:
    def __init__(self, last_update, list_room):
        self.last_update = last_update
        self.list_room = list_room

class Room:
    def __init__(self, room_name, room_area, room_description, number_of_room, number_of_bathroom, number_of_bedroom, room_capacity, bedtype, tv_and_ubc, jacuzzi, DVDplayer, fridge, air_conditioner):
        self.room_name = room_name
        self.room_area = room_area
        self.room_description = room_description
        self.number_of_room = number_of_room
        self.number_of_bathroom = number_of_bathroom
        self.number_of_bedroom = number_of_bedroom
        self.room_capacity = room_capacity
        self.bedtype = bedtype
        self.tv_and_ubc = tv_and_ubc
        self.jacuzzi = jacuzzi
        self.DVDplayer = DVDplayer
        self.fridge = fridge
        self.air_conditioner = air_conditioner

class Roominfo:
    def __init__(self, room_number, room_user, guests_in_room, room_checkin_date, room_checkout_date, room_changes):
        self.room_number = room_number
        self.room_user = room_user
        self.guests_in_room = guests_in_room
        self.room_checkin_date = room_checkin_date
        self.room_checkout_date = room_checkout_date
        self.room_changes = room_changes


class Roomstatus:
    def __init__(self, available, on_request, fully_booked):
        self.available = available
        self.on_request = on_request
        self.fully_booked = fully_booked


class Showroom:
    def __init__(self, room_number, room_checkout_date, room_name):
        self.room_number = room_number
        self.room_checkout_date = room_checkout_date
        self.room_name = room_name

##

class Accout:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class User:
    def __inti__(self, title, name, surname, address):
        self.title = title
        self.name = name
        self.surname = surname
        self.address = address

##


class Payment:
    def __inti_(self, credit_card, qr_payment):
        self.credit_card = credit_card
        self.qr_payment = qr_payment


class Creditcard:
    def __inti__(self, card_number, cardholder_name, expiry_date, cvv, country, bank, email):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.country = country
        self.bank = bank
        self.email = email


class Qrpayment:
    def __inti__(self, qrcode_pic):
        self.qrcode_pic = qrcode_pic


class Paymentstatus:
    def __init__(self, complete, incomplete):
        self.complete = complete
        self.incomplete = incomplete


class Booking:
    def __init__(self, date_in, date_out, country):
        self.date_in = date_in
        self.date_out = date_out
        self.country = country

class Bookingstatus:
    def __init__(self, pending, confirm, cancel):
        self.pending = pending
        self.confirm = confirm
        self.cancel = cancel

class Bookingsummary:
    def __inti__(self, room_number, price, night):
        self.room_number = room_number
        self.price = price
        self.night = night


class Hotel:
    def __init__(self, destination, residence, offer, experiences, event_or_meeting):
        self.destination = destination
        self.residence = residence
        self.offer = offer
        self.experiences = experiences
        self.event_or_meeting = event_or_meeting


class Admin:
    def __init__(self):