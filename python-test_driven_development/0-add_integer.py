#!/usr/bin/python3
""" This module will add two integers"""


def add_integer(a, b=98):
    """ This is the function that will add"""

    a = int(a)
    b = int(b)

    if not isinstance(a, int):
        print("a must be an integer")
    elif not isinstance(b, int):
        print("b must be an integer")
    else:
        return a + b
