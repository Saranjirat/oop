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

xiw.add_room(r.room_plantationview,testalog)
xiw.add_room(r.room_horizonview)