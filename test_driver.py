# -*- coding: utf-8 -
import os
import sys

cur_path = os.path.dirname(os.path.realpath(__file__))

os.putenv("PYTHONPATH", cur_path)


def run_case(input_argv=""):
    case_path = os.path.join(cur_path, "Input")

    lst = os.listdir(case_path)
    for c in lst:
        if os.path.splitext(c)[1] == '.txt':
            print(c)
            if input_argv:
                os.system('python main.py {} {}'.format(os.path.join(case_path, c), input_argv))
            else:
                os.system('python main.py {}'.format(os.path.join(case_path, c)))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        argv = sys.argv[1]
        run_case(argv)
    else:
        run_case()
    # run_case()

