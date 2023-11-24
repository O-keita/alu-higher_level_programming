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
    """ class documented"""

    def __init__(self, radius):
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
