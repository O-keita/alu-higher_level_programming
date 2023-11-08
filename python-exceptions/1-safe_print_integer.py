#!/usr/bin/python3
def safe_print_integer(value):
    val = value == int
    try:
        print("{:d}".format(value))
    except:
        print("{} is not an integer".format(value))
    return val
