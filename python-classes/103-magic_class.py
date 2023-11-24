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

# Example instantiation and usage
if __name__ == "__main__":
    # Instantiate MagicClass with a radius value
    circle = MagicClass(5.0)

    # Example usage:
    area_result = circle.area()
    circumference_result = circle.circumference()

    print(f"Radius: {circle._MagicClass__radius}")  # Accessing the private attribute
    print(f"Area: {area_result}")
    print(f"Circumference: {circumference_result}")
