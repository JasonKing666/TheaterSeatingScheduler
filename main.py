import sys

from file_process import parse_input, write_output
from Scheduler.worst_fit_scheduler import WorstFitScheduler
from Scheduler.first_fit_scheduler import FirstFitScheduler


ROWS = 10
COLS = 20
COL_SPACE = 3
ROW_SPACE = 1
OUTPUT_PATH = "Output/"
OUTPUT_NAME = "output"
ROW_CHAR_DICT = {i: chr(ord('A') + i) for i in range(ROWS)}


def main(input_file_path, input_scheduler_type="WorstFit"):
    reservation_orders = parse_input(input_file_path)

    if input_scheduler_type == "WorstFit":
        scheduler = WorstFitScheduler(reservation_orders, COL_SPACE, ROWS, COLS, ROW_CHAR_DICT)
    elif input_scheduler_type == "FirstFit":
        scheduler = FirstFitScheduler(reservation_orders, COL_SPACE, ROWS, COLS, ROW_CHAR_DICT)

    scheduler.schedule_orders()
    output_file_path = write_output(OUTPUT_PATH + input_scheduler_type + '/', OUTPUT_NAME, input_file_path, reservation_orders)
    print("/".join(input_file_path.split("/")[:-2]) + "/" + output_file_path)


if __name__ == "__main__":
    file_path = sys.argv[1]
    if len(sys.argv) == 3:
        scheduler_type = sys.argv[2]
        main(file_path, scheduler_type)
    else:
        main(file_path)
