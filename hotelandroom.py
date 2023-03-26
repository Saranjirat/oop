class Hotel:
    def __init__(self, destination, the_residences, offer, experiences,event_meeting,roomlist):
        self.__destination = destination
        self.__the_residences = the_residences
        self.__offer = offer
        self.__experiences =  experiences
        self.__event_meeting = event_meeting
        self.__roomlist = []
    


class Room:
    def __init__(self, room_name, room_area, number_bathroom, number_bedroom, room_capacity, bedtype, room_amendities):
        self._room_name = room_name
        self._room_area = room_area
        self._number_of_bathroom = number_bathroom
        self._number_of_bedroom = number_bedroom
        self._room_capacity = room_capacity
        self._bedtype = bedtype
        self._room_amenities = room_amendities
           



class Roomcatalog(Room):
    def __init__(self, room_list):
        self.__room_list = []




class Reservetime:
    def __init__() 


kirimaya = Hotel("Kirimaya,"a",[])
##kiri

room_plantationview = Room("Plantation View","42 sq. m.","1 Bedroom","1 Room", "3 Persons(2 Adults + 1 Child)", "Double or Twin",
                           "-Balcony daybed with a view,-Cable TV,-LCD screen in Suites and Villas,DVD/ CD players")

room_horizonview = Room("Horizon View","42 sq. m.","1 Bedroom","1 Room","3 Persons (2 Adults + 1 Child)","Double or Twin",
                        "-Balcony daybed with a view,-Cable TV,-LCD screen in Suites and Villas,-DVD/ CD players")

room_terrace_suite = Room("Terrace Suite","84 sq. m.","1 Bedroom","1 Room","3 Persons (2 Adults + 1 Child)","Double or Twin")


##muthi

room_muthimaya_forest_poolvilla = Room("MUTHI MAYA Forest Pool Villa","164 sq. m.","1 Bedroom","1 Room"," 3 Persons (2 Adults + 1 Child)","Double Bed")


##atta

room_one_bedroom_suite = Room("One Bedroom Suite","65 sq. m.","1 Bedroom","1 Room")

room_one_bedroom_delight = Room("One Bedroom Delight","65 sq. m.","1 Bedroom","1 Room")

room_two_bedroom_delight = Room("Two Bedroom Delight","102 sq. m.","2 Bedroom","2 Room")

room_penthouse_suite = Room("Penthouse Suite","235 sq. m.","2 Bedroom","2 Room")

roomnow = Roomcatalog

