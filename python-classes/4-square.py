#!/usr/bin/python3
"""The Sqaure clasee"""


class Square:
    """ initialize the instances"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):

        """calculating area"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """getter for retrieving"""

        return self.__size
    @size.setter
    def size(self, new_size):
        """ changing the value"""
        self.__size = new_size



        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = new_size
