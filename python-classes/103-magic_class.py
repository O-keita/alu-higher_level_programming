#!/usr/bin/python3
"""
MagicClass: Circle calculations.

Attributes:
    __radius (float): The circle's radius.

Methods:
    __init__(self, radius): Initializes MagicClass with a given radius.
    area(self): Returns the circle's area.
    circumference(self): Returns the circle's circumference.
"""

import math

class MagicClass:
    """ Okay it is documented now"""

    def __init__(self, radius):
        """
        Initializes MagicClass with a given radius.

        Args:
            radius (float): The circle's radius.
        """
        self.__radius = 0
        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the circle's area."""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Returns the circle's circumference."""
        return 2 * math.pi * self.__radius
