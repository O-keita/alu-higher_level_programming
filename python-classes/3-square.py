#!/usr/bin/python3
""" We will try creating a class Square"""


class Square:
    """ Let's initialize the class below"""

    def __init__(self, size):
        """checking if the type size is integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        return self.size * self.size
