#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """ Let's use append to return num of char"""

    with open(filename, 'a', encoding='utf-8') as file:
        char = file.write(text)
    return char
