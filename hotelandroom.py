class Hotel:
    def __init__(self, destination, the_residences, offer, experiences,event_meeting,roomlist):
        self.__destination = destination
        self.__the_residences = the_residences
        self.__offer = offer
        self.__experiences =  experiences
        self.__event_meeting = event_meeting
        self.__roomlist = []
    


class Room:
    def __init__(self, name, area, number_bathroom, number_bedroom, capacity, bedtype, amendities):
        self._name = name
        self._area = area
        self._number_bathroom = number_bathroom
        self._number_bedroom = number_bedroom
        self._capacity = capacity
        self._bedtype = bedtype
        self._amenities = amendities
           


class Roomcatalog(Room):
    def __init__(self, room_list):
        self.__room_list = []


class Shoppingcart():
    def __init__(self, cart):
        self._cart = []
