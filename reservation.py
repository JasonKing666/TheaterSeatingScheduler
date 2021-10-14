class Reservation:
    """Will be used to create reservation objects containing id, number of seats"""
    def __init__(self, identifier_id, num_seats, order_number):
        self.id = identifier_id
        self.num_seats = num_seats
        self.seat_assignments = ""
        self.order_number = order_number

    def set_seat_assignments(self, labels):
        self.seat_assignments = labels

    def update_seat_assignments(self, line_char, start_index):
        self.seat_assignments = ",".join([line_char + str(index + 1)
                                          for index in range(start_index, start_index + self.num_seats)])


class ReservationOrders:
    """Will be used to store reservations"""
    def __init__(self, reservation_orders=[]):
        self.reservation_orders = reservation_orders

    def add_reservation_order(self, reservation_order):
        self.reservation_orders.append(reservation_order)

    def sort_reservation_orders(self):
        """
            sort the orders by their seat_demand, if same, put the smaller id request in the front
        """
        self.reservation_orders.sort(key=lambda x: (-x.num_seats, x.order_number))

    def get_reservation_orders(self):
        return self.reservation_orders
