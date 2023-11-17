#!/usr/bin/python3
""" We are creating a Rectangle object that take w and h"""


class Rectangle:
    """ We will initialize our private variables """

    def __init__(self, width = 0, height = 0):
        """ the initialization"""

        if not isinstance(width, int):
            """ making sure width is an integer"""
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            """ making sure height is an integer"""
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if width < 0:
            raise ValueError("width must be >= 0")
            """initialization"""
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """ Getter for width"""
        return self.__width
    @width.setter
    def width(self, value):
        """Setter for width"""
        
        self.__width = value
    @property
    def height(self):
        """ getter for height"""

        return self.__height
    @height.setter
    def height(self, value):
        """ Setter for height"""

        self.__height = value
        
