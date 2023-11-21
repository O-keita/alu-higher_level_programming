#!/usr/bin/python3
""" class about rectangle"""


class Rectangle:
    """ initialize instances"""

    def __init__(self, width=0, height=0):
        """ Initilize """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += "#" * self.width
            if i < self.height - 1:
                result += "\n"
        return result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

# Example usage:
rectangle = Rectangle(4, 3)
print(rectangle.area())       # Output: 12
print(rectangle.perimeter())  # Output: 14
print(str(rectangle))
# Output:
# ####
# ####
# ####
print(repr(rectangle))        # Output: Rectangle(4, 3)

