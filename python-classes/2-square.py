#!/usr/bin/python3
""" defining the fuction sqaure and instantiate the variables"""


class Square:
    """Here we instantiate the variables below"""

    def __init__(self, size=0):
        """Here we initialize the variable size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self._Square__size = size
