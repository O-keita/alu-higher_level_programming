#!/usr/bin/python3
""" Printing squares with #"""


def print_square(size):
    """ def print_square(size):
     will print squares
     """

     if not isinstance(size, int):
         raise TypeError("size must be an integer")
     if size < 0:
         raise ValueError("size must be >= 0")
     if isinstance(size, float) and size < 0:
         raise TypeError("size must be an integer")
     print((("#" * size +"\n") * size), end ="")
