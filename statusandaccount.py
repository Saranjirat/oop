class Paymentstatus(Enum):
    COMPLETE, INCOMPLETE = 1,2

class Bookingstatus(Enum):
    PENDING, COMFIRM, CANCEL = 1,2,3

class Roomstatus(Enum):
    AVAILBLE, FULL, ON_REQUEST = 1,2,3
        

##person

class Accout:
    def __init__(self, email, password):
        self._email = email
        self._password = password

class User:
    def __inti__(self, title, name, surname, address):
        self.__title = title
        self.__name = name
        self.__surname = surname
        self.__address = address

class Guest:
    def __init__(self):

class Admin:
    def __init__(self):