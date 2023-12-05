#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """
    Class that defines a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size+), position=(0, 0)): Initializes a new instance
        of the Square class.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square with the character #.

    Properties:
        size: Getter and setter for the size attribute.
        position: getter and setter for the position attribute.

    Raises:
        TypeError: If size is not an integer or positions is not a tuple of 2
        positive integers.
        ValueError: If size is less than 0 or position contains non-positive
        integers.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TYpeError: If size is not an integer or position is not a tuple of
            2 positive integers.
            ValueError: If size is less than 0 or position contains
            non-positive integers.
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2 or not
        all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
