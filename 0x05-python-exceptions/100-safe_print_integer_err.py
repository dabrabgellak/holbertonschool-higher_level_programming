#!/usr/bin/python3
import sys

def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
    except Exception:
        return False
        sys.stderr.write("Exception: ")
    else:
        return True
