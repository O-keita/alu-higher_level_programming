#!/usr/bin/python3
""" 7-base_geometry.py: Validator"""


class BaseGeometry:
    """ our functions will follow below"""

    def area(self):
        """ I have documentation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ fuck decumentations"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
