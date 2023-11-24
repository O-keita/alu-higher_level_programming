#!/usr/bin/python3
""" module documented"""


class Square:
    """ class documented"""

    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(n, int) and n > 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self._position = value

    def area(self):
        return self._size ** 2

    def my_print(self):
        if self._size == 0:
            print()
            return

        for _ in range(self._size):
            print("#####" if self._position[1] == 0 else " " * self._position[1] + "#####")

    def __str__(self):
        self.my_print()
