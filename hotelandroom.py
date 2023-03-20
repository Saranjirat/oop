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


