#!/usr/bin/python3
""" myInt class """


class MyInt(int):
    """ initialization"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
