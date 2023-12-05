#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """
    Class that defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square using the character #.

    Properties:
        size: Getter and setter for the size attribute.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """Intializes anew instance of the Square class.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
