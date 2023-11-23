#!/usr/bin/python3
""" 1-write_file.py"""


def write_file(filename="", text=""):
    """ write the file with w"""

    with open(filename, 'w', 'utf-8') as file:
        words = file.write(text)

        char = len(words)
        return char
