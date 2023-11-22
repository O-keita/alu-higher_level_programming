#!/usr/bin/python3
""" Checking for Instances """


def is_same_class(obj, a_class):
    """ Now checking the instances"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
