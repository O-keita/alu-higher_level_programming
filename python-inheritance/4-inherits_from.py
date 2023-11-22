#!/usr/bin/python3
"""using the subclass"""


def inherits_from(obj, a_class):
    """ checking if obj is a subclass of a_class"""

    if issubclass(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
