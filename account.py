from Roomcatalog import Roomcatalog
class account:
    def __init__(self,contact_name,contact_username,contact_phone_num,contact_email,contact_password):
        self._contact_name= contact_name
        self._contact_username = contact_username
        self._contact_phone_num = contact_phone_num
        self._contact_email = contact_email
        self._contact_password = contact_password
        

class customer(account):
    def __init__(self, contact_name, contact_username, contact_phone_num, contact_password, contact_email):
        super().__init__(contact_name, contact_username, contact_phone_num, contact_password, contact_email)

    def select_room(self,room):
        self._choose_room=room    