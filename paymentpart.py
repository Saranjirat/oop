class Payment:
    def __inti__(self, credit_card, status):
        self.__credit_card = credit_card
        self.__status = status


class Creditcard:
    def __inti__(self, card_number, cardholder_name, expiry_date, cvv, country, bank, email):
        self.__card_number = card_number
        self.__cardholder_name = cardholder_name
        self.__expiry_date = expiry_date
        self.__cvv = cvv
        self.__country = country
        self.__bank = bank
        self.__email = email


class Promotion:
    def __init__(self, code):
        self.__code = code


class Booking:
    def __init__(self, date_in, date_out, promotion_code, status):
        self.__date_in = date_in
        self.__date_out = date_out
        self.__country = promotion_code
        self.__status = status


class BookingHistory:
    def __init__(self, booking_detail):
        self.__booking_detail = booking_detail