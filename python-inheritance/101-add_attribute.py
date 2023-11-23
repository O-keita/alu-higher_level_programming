#!/usr/bin/python3
""" Attribute class """


class MyClass:
    pass

def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Parameters:
    - obj: The object to which the attribute will be added.
    - attr_name: The name of the new attribute.
    - attr_value: The value of the new attribute.

    Raises:
    - TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        error_message = "can't add new attribute"
        print(f"Error: {error_message}")
        raise TypeError(error_message)

    setattr(obj, attr_name, attr_value)
