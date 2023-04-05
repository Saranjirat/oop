from Roomcatalog import Roomcatalog
from room import Room
class account:
    def __init__(self,contact_name,contact_username,contact_phone_num,contact_email,contact_password):
        self._contact_name= contact_name
        self._contact_username = contact_username
        self._contact_phone_num = contact_phone_num
        self._contact_email = contact_email
        self._contact_password = contact_password
    
    def watch_room(self, Roomcatalog, hotel_name):
        tamp_rooms_lists = []
        for i in Roomcatalog:
            if hotel_name == "Kirimayaresort" and i._hotel_name == "Kirimayaresort" :
                tamp_rooms_lists = [room for room in Roomcatalog._room_lists if room.get_hotel_name() == "Kirimayaresort" ]
                return tamp_rooms_lists 
            elif hotel_name == "Muthimaya" :
                tamp_rooms_lists = [room for room in Roomcatalog._room_lists if room.get_hotel_name() == "Muthimaya" ]
                return tamp_rooms_lists
            elif hotel_name == "Atta" :
                tamp_rooms_lists = [room for room in Roomcatalog._room_lists if room.get_hotel_name() == "Atta" ]
                return tamp_rooms_lists
        
        

class customer(account):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)

    def select_room(self,room):
        self._choose_room=room    

    def search_room(self,):
        pass

class admin(account):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)

    def add_room(self,room,room_catalog:Roomcatalog):
        room_catalog._room_lists.append(room)

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