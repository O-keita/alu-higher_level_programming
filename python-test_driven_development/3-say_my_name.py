#!/usr/bin/python3
""" Printing names """


def say_my_name(first_name, last_name=""):
    """ The function will take first and last name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    result = print(f"My name is {first_name} {last_name}")
    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
