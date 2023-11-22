#!/usr/bin/python3
""" Sorted the object"""


class MyList(list):
    """ define the sorted function"""

    def print_sorted(self):
        sorted_list = sorted(self)
        return sorted_list
