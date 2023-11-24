#!/usr/bin/python3
""" class docummented"""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the
        square as a tuple of 2 positive integers.

    Methods:
        __init__(self, size=0, position=(0, 0)):
        Initializes a new Square instance.
        area(self): Calculates and returns the
        area of the square.
        my_print(self): Prints the square using
        '#' characters, considering the size and position.

    Properties:
        size: Gets or sets the size of the square.
        position: Gets or sets the position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the
            square as a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square
            as a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the
            square as a tuple of 2 positive integers.

        Raises: TypeError: If position is not a tuple of 
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int)\
                for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the 
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """

        Returns:
            str: The string representation of the square.
        """
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip()

if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
