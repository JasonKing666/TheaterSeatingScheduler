from base_scheduler import BaseScheduler


class FirstFitScheduler(BaseScheduler):
    """
        For given requests, we process the quests following their given order
        Every seat request, try to put it from last row to the first row, from start of every row
        Find the first row which could satisfy this seat request and process next request
    """

    def __init__(self, reservation_orders, seats_buffer, row_number, col_number, row_char_dict):
        self.reservation_orders = reservation_orders
        self.seats_buffer = seats_buffer
        self.row_number = row_number
        self.col_number = col_number
        self.row_char_dict = row_char_dict

        self.remaining_seats = [col_number] * row_number

    def schedule_orders(self):
        for reservation in self.reservation_orders.get_reservation_orders():
            for row in range(self.row_number - 1, -1, -1):

                curr_remaining_seat = self.remaining_seats[row]
                is_row_empty = curr_remaining_seat == self.col_number

                # there are no any row has enough empty seat for this reservation order
                if is_row_empty and reservation.num_seats > curr_remaining_seat:
                    continue

                if not is_row_empty and reservation.num_seats + self.seats_buffer > curr_remaining_seat:
                    continue

                if not is_row_empty:
                    curr_remaining_seat -= self.seats_buffer

                line_char = self.row_char_dict[row]
                reservation.update_seat_assignments(line_char, self.col_number - curr_remaining_seat)
                curr_remaining_seat -= reservation.num_seats
                self.remaining_seats[row] = curr_remaining_seat
                break
