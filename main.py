
import datetime
from Roomcatalog import Roomcatalog
from room import Room
from booking import Booking
from account import customer
from account import admin
from Interval import interval
import roominstance as r 



testalog = Roomcatalog()

xiw = admin("xiw",
            "tarijnaras",
            "0950988592",
            "xiwijnaras",
            "xiw1234")

mix = customer("mix",
               "saranji",
               "0627370763",
               "mixsaranji",
               "mix1234") 

xiw.add_room(r.room_plantationview,testalog)
xiw.add_room(r.room_horizonview,testalog)
xiw.add_room(r.room_terrace_suite,testalog)
xiw.add_room(r.room_muthimaya_forest_poolvilla,testalog)
xiw.add_room(r.room_one_bedroom_suite,testalog)
xiw.add_room(r.room_one_bedroom_delight,testalog)
xiw.add_room(r.room_two_bedroom_delight,testalog)
xiw.add_room(r.room_penthouse_suite,testalog)




for i in range(len(mix.watch_room(testalog,"Kirimayaresort"))):
    print(mix.watch_room(testalog, "Kirimayaresort",datetime.datetime(2023, 6, 8, 10, 0),datetime.datetime(2023, 6, 9, 10, 0))[i].get_room_name())

r.room_plantationview.add_interval(interval(datetime.datetime(2023, 6, 8, 10, 0),datetime.datetime(2023, 6, 9, 10, 0)))
r.room_horizonview.add_interval(interval(datetime.datetime(2023, 6, 8, 10, 0),datetime.datetime(2023, 6, 9, 10, 0)))
r.room_terrace_suite.add_interval(interval(datetime.datetime(2023, 6, 8, 10, 0),datetime.datetime(2023, 6, 9, 10, 0)))

# r.room_plantationview.add_interval(interval(datetime.datetime(2018, 6, 8, 10, 0),datetime.datetime(2018, 6, 9, 10, 0)))
# r.room_horizonview.add_interval(interval(datetime.datetime(2018, 6, 8, 10, 0),datetime.datetime(2018, 6, 9, 10, 0)))
# for i in r.room_plantationview._date_not_available: 
#     print(i.get_start_time())
#     print(i.get_end_time())
# print(testalog.find_available_room("8-6-2018","0:00","9-6-2018","0:00"))
