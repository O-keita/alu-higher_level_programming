#!/usr/bin/python3
""" This module will add two integers"""


def add_integer(a, b=98):
    """ This is the function that will add"""
    if not isinstance(a, int) or not isinstance(a, float):
        print("a must be an integer")
    elif not isinstance(b, int) or not isinstance(b, float):
        print("b must be an integer")
    else:
        return a +b
