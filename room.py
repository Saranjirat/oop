class Room:
    def __init__(self, room_name, room_area, number_bedroom, number_bathroom, date_not_avalible, room_amount):
        self._room_name = room_name
        self._room_area = room_area
        self._number_of_bathroom = number_bedroom
        self._number_of_bedroom = number_bathroom
        self._date_not_avalible = date_not_avalible
        self._room_amount = room_amount
        self._interval_list = []

    def add_interval(self,interval):
        self._interval_list.append(interval)

    def check_no_overlap(start_time1, end_time1, start_time2, end_time2) :
        if start_time1 > end_time2 or start_time2 > end_time1:
            return True
        else :
            return False
        
    def room_available(self, datetime1, datetime2):
        for i in self._interval_list :
            if not self.check_no_overlap(i.get_start_time, i.get_end_time, datetime1, datetime2):
                return False
        return True
    
class Interval :
    def __init__(self, start_time,end_time):
        self._start_time
    
