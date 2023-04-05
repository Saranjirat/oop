from datetime import datetime
from room import Room
class Roomcatalog:
    def __init__(self):
        self._room_lists = []
        self._check = True

    def show_catalog(self):
        for i in self._room_lists:
            print(i)
    
    def find_available_room(self, start_date, start_time, end_date, end_time):
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_room = []
        available_bathroom = []
        available_room_all = {}
        j = 0
        for i in self._room_lists:
            if not i._status_available:
                continue
            if not i.room_available(date1, date2):
                continue
            # available_room.append(i._room_name)
            # available_bathroom.append(i._number_of_bathroom)
            available_room_all[j] = [i._room_name,i._number_of_bathroom]
            j += 1
        return available_room_all
   

