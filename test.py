import datetime
from Roomcatalog import Roomcatalog
from room import Room
from booking import Booking
from account import customer
from account import admin
from Interval import interval

room_plantationview = Room("Plantation View",
                           "42 sq. m.",
                           "1 Bedroom",
                           "1 Room",
                           [],
                            "2000"
                            )
room_horizonview = Room("Horizon View",
                        "42 sq. m.",
                        "1 Bedroom",
                        "1 Room",
                        [],
                        "3000"
                        ) 
mix = customer("mix",
               "saranji",
               "0627370763",
               "mixsaranji",
               "mix1234") 

xiw = admin("xiw",
            "tarijnaras",
            "0950988592",
            "xiwijnaras",
            "xiw1234")

start_date= "19-6-2023"
start_time=  "12:30"
testalog = Roomcatalog()
xiw.add_room(room_plantationview,testalog)
xiw.add_room(room_horizonview,testalog)
room_plantationview.add_interval(interval(datetime.datetime(2018, 6, 8, 10, 0),datetime.datetime(2018, 6, 9, 10, 0)))
room_horizonview.add_interval(interval(datetime.datetime(2018, 6, 8, 10, 0),datetime.datetime(2018, 6, 9, 10, 0)))
for i in room_plantationview._date_not_available: 
    print(i.get_start_time())
    print(i.get_end_time())
print(testalog.find_available_room("8-6-2018","0:00","9-6-2018","0:00"))
