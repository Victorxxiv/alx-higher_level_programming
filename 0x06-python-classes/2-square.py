#!/usr/bin/python3
"""Defirnes a class Square."""


class Square:
    """
    Class that defines a square.

    Attributes:
         __size (int): The size of the square.

     Methods:
          __intit__(self, size=0): Initializes a new instance of Square class.

     Raises:
          TypeError: If size is not an integer.
          ValueError: If size is less than 0.
     """

    def __init__(self, size=0):
        """INitializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
