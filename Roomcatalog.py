from datetime import datetime
from room import Room
from booking import Booking
class Roomcatalog:
    def __init__(self):
        self._room_lists = []
        self._check = True

    def add_room(self,room):
        self._room_lists.append(room)

    def show_catalog(self):
        for i in self._room_lists:
            print(i._room_name)
    
    def find_available_room(self, start_date, start_time, end_date, end_time, hotel):
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_room = []
        available_room_all = {}
        j = 0
        for i in self._room_lists:
            if not i._status_available and i._hotel_name == hotel:
                continue
            if not i.room_available(date1, date2) and i._hotel_name == hotel:
                continue
            if not i._hotel_name == hotel:
                continue
            available_room.append(i)
            # available_bathroom.append(i._number_of_bathroom)
            available_room_all[j] = [i._room_name,i._number_of_bathroom]
            j += 1
        return available_room
    
    def book_room(self, subject, room, user, st_date, end_date):
        
        for i in self._room_lists:
            if i._room_name == room:
                book_room = i
                break
        interval = Interval(st_date, end_date)
        book_room.add_interval(interval)
        booking = Booking()
        
        
        return "success"
   


class Interval:
    def __init__(self, start_date, start_time, end_date, end_time):
        self.__start_time = self.convert_str_datetime_to_datetime(
            start_date, start_time)
        self.__end_time = self.convert_str_datetime_to_datetime(
            end_date, end_time)

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return (self.__end_time)

    def __str__(self):
        return self.convert_datetime_to_str_datetime(self.__start_time)+" "+self.convert_datetime_to_str_datetime(self.__end_time)

    def convert_str_datetime_to_datetime(self, str_date, str_time):
        return datetime.strptime(str_date + " " + str_time, '%d-%m-%Y %H:%M')

    def convert_datetime_to_str_datetime(self, datetime):
        return datetime.strftime("%m/%d/%Y, %H:%M")