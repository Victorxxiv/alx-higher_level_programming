#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py)

    Attributes:
         size: size of a square (1 side).
    """

    def __init__(self, size):
        """"Initialization method with size (no type/value verification).

        Args:
             size : The size of the square.

        """
        self.__size = size
