#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except:
        sys.stderr.write("Exception: {}".format(sys.exc_info()[0]))
        return False
    else:
        return True
