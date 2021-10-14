from reservation import Reservation
from reservation import ReservationOrders


def parse_input(filename):
    """ parses input file, return list of reservation request """
    reservation_orders = ReservationOrders()
    with open(filename, 'r') as f:

        for i, line in enumerate(f.readlines()):
            identifier, number = line.split()
            reservation_orders.add_reservation_order(Reservation(identifier, int(number), i))
    return reservation_orders


def write_output(output_path, output_prefix, input_file_name, reservation_orders):
    """ output result file containing seating assignments for each request"""
    file_name = output_path + output_prefix + input_file_name.split("/")[-1][5:]
    with open(output_path + output_prefix + input_file_name.split("/")[-1][5:], 'w') as f:
        for reservation_order in sorted(reservation_orders.get_reservation_orders(), key=lambda x: x.id):
            f.write("%s\n" % str(reservation_order.id + " " + reservation_order.seat_assignments))
    return file_name
