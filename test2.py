import datetime
from Roomcatalog import Roomcatalog
from room import Room
from Interval import interval
from account import customer

room_plantationview = Room("Plantation View",
                           "42 sq. m.",
                           "1 Bedroom",
                           "1 Room",
                           [datetime.datetime(2018, 6, 1, 0, 0), datetime.datetime(2018, 6, 2, 0, 0), 
                            datetime.datetime(2018, 6, 5, 0, 0), datetime.datetime(2018, 6, 6, 0, 0),
                            datetime.datetime(2018, 6, 7, 0, 0),datetime.datetime(2018, 6, 8, 0, 0), 
                            datetime.datetime(2018, 6, 9, 0, 0), datetime.datetime(2018, 6, 10, 0, 0)],
                            "2000")
room_horizonview = Room("Horizon View",
                        "42 sq. m.",
                        "1 Bedroom",
                        "1 Room",
                        [datetime.datetime(2018, 6, 1, 0, 0), datetime.datetime(2018, 6, 2, 0, 0), 
                        datetime.datetime(2018, 6, 5, 0, 0), datetime.datetime(2018, 6, 6, 0, 0),
                        datetime.datetime(2018, 6, 7, 0, 0),datetime.datetime(2018, 6, 8, 0, 0), 
                        datetime.datetime(2018, 6, 9, 0, 0), datetime.datetime(2018, 6, 10, 0, 0)],
                        "3000") 
mix = customer("mix",
               "saranji",
               "0627370763",
               "mixsaranji",
               "mix1234") 

mix.add_time(datetime.datetime(2018, 6, 3, 0, 0),datetime.datetime(2018, 6, 5, 0, 0))
room = room_available()