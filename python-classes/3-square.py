#!/usr/bin/python3
""" We will try creating a class Square"""


class Square:
    """ Let's initialize the class below"""

    def __init__(self, size=0):
        """checking if the type size is integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculating the area of the the square"""
        return (self.__size * self.__size)
