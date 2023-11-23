#!/usr/bin/python3
"""Geometry class below"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Initialization"""

    def __init__(self, width, height):
        """ Validation """
        self.integer_validator("width", width)
        self.integer_validator("width", height)
        self.__width = width
        self.__height = height
