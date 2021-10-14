from base_scheduler import BaseScheduler
import heapq


class WorstFitScheduler(BaseScheduler):
    """
        For given requests, we process the quests from largest seat demand to smallest
        Every seat request after sort, try to put it in the most empty row, from start of this row
    """

    def __init__(self, reservation_orders, seats_buffer, row_number, col_number, row_char_dict):
        self.reservation_orders = reservation_orders
        self.seats_buffer = seats_buffer
        self.satisfied_row_heap = []
        self.row_number = row_number
        self.col_number = col_number
        self.row_char_dict = row_char_dict

        self._build_initial_satisfied_row_heap()

    def _build_initial_satisfied_row_heap(self):
        remaining_seat = self.col_number
        for row_num in range(self.row_number):
            # use number to change min heap to max heap
            heapq.heappush(self.satisfied_row_heap, [-remaining_seat, -row_num])

    def schedule_orders(self):
        # sort the orders by their seat_demand, if same, put the smaller id request in the front
        self.reservation_orders.sort_reservation_orders()

        for reservation in self.reservation_orders.get_reservation_orders():
            # the peak of heap is the most empty row
            is_row_empty = -self.satisfied_row_heap[0][0] == self.col_number

            # there are no any row has enough empty seat for this reservation order
            if is_row_empty and reservation.num_seats > -self.satisfied_row_heap[0][0]:
                continue
            if not is_row_empty and reservation.num_seats + self.seats_buffer > -self.satisfied_row_heap[0][0]:
                continue

            # pop most empty row from heap
            current_row = heapq.heappop(self.satisfied_row_heap)
            if not is_row_empty:
                current_row[0] += self.seats_buffer

            # use this row to satisfy current sear request
            line_char = self.row_char_dict[-current_row[1]]
            reservation.update_seat_assignments(line_char, self.col_number + current_row[0])
            current_row[0] += reservation.num_seats
            heapq.heappush(self.satisfied_row_heap, current_row)