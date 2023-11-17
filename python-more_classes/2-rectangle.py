#!/usr/bin/python3
""" class about Rectangle """


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with type and value checking"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with type and value checking"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """ Calculate the area by w * h"""

        return self.__width * self.__height

    def perimeter(self):
        """ Calculate perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width *2) + (self.__height))
    
