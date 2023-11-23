#!/usr/bin/python3
""" creating a student class"""


class Student:
    """ we initialize the variables below"""

    def __init__(self, first_name, last_name, age):
        """ arge:
            first name
            last name
            student age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__obj__
