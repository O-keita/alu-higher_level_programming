#!/usr/bin/python3
""" Geometry class with just and exception"""


class BaseGeometry:
    """ lets inititialize"""

    def area(self):
        raise Exception("area() is not implemented")
