
class BaseScheduler(object):

    def __init__(self, reservation_orders, seats_buffer, row_number, col_number, row_char_dict):
        self.reservation_orders = reservation_orders
        self.seats_buffer = seats_buffer
        self.satisfied_row_heap = []
        self.row_number = row_number
        self.col_number = col_number
        self.row_char_dict = row_char_dict

    def schedule_orders(self):
        pass
