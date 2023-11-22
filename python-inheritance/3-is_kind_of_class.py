#!/usr/bin/python3
""" Checking the instance"""


def is_kind_of_class(obj, a_class):
    """ We will check if obj is an istance"""
    """ of a_class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
