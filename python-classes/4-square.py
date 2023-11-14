#!/usr/bin/python3
"""The Sqaure clasee"""


class Square:
    """ initialize the instances"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            """ checking if size is integer"""
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        """ actual Initialization"""
        self.__name = name
    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, new_size):
        self.__size = new_size
