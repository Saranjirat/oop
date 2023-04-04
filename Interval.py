import datetime

class interval :
    def __init__(self,start_time, end_time):
        self.__start_time = start_time
        self.__end_time = end_time

    def check_no_overlap(start_time1, end_time1, start_time2, end_time2) :
        if start_time1 > start_time2 or start_time2 > end_time2:
            return True
        else :
            return False
        
    def room_available(self, datetime1, datetime2):
        for i in self.__interval_list :
            if not self.check_no_overlap(i.get_start_time, i.get_end_time, datetime1, datetime2):
                return False
        return True
    
    def __str__(self):
        return(f"Room id : {self.__id} capacity {self.__capacity}")
    
    def find_available_room(self, start_date, start_time, end_date, end_time, capacity):
        date1 = datetime.strptime(start_date + " "+ start_time, '%d-%m-%y %H:%M')
        date2 = datetime.strptime(end_date + " "+ end_time, '%d-%m-%y %H:%M')
        available_room = []
        for i in self.__meeting_room_list:
            if not i.is_available:
                continue
            if not i.room.avaliable(date1, date2):
                continue
            available_room.append(i)
        return available_room
