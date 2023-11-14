#!/usr/bin/python3
""" defining the fuction sqaure and instantiate the variables"""


class Square:
    """Here we instantiate the variables below"""

    def __init__(self,size=0):
        """ Here we initialize the variable size"""

        assert(isinstance(size, int))

        self.size = size
