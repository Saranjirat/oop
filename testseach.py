from datetime import datetime
class MeetingScheduler:
    def __init__(self):
        self.__meeting_room_list = []
        self.__user_list = []

    def add_room(self, room):
        self.__meeting_room_list.append(room)

    def find_available_room(self, start_date, start_time, end_date, end_time, capacity):
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_room = []
        for i in self.__meeting_room_list:
            if not i.is_available:
                continue
            if i.capacity < capacity:
                continue
            if not i.room_available(date1, date2):
                continue
            available_room.append(i)
        return available_room
    
    def list_room(self):
        for i in self.__meeting_room_list:
            print(i)

class Interval:
    def __init__(self, start_time, end_time):
        self.__start_time = start_time
        self.__end_time = end_time

class Calendar:
    def __init__(self):
        self.__meeting_list = []

    def is_available(self):
        return self.__is_available
    
    def add_interval(self, interval):
        self.__interval_list.append(interval)

    def check_no_overlap(start_time1, end_time1, start_time2, end_time2):
        if start_time1 > end_time2 or start_time2 > end_time1:
            return True
        else:
            return False

    def room_available(self, datetime1, datetime2):
        for i in self.__interval_list:
            if not self.check_no_overlap(i.get_start_time, i.get_end_time, datetime1, datetime2):
                return False
        return True
