import datetime
from Roomcatalog import Roomcatalog
from room import Room
from booking import Booking
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
testalog = Roomcatalog([room_plantationview,room_horizonview])
testalog.checktime_room(mix._time_start,mix._time_out)
print(testalog._avalible)
mix.select_room(room_plantationview)
print(mix._choose_room)
bookmix=Booking(mix._time_start,mix._time_out,100)
print(bookmix._date_in)
print(bookmix._date_out)


