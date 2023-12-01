#!/usr/bin/python3

class Square:
    """Class that defines a square."""

    def __init__(self,size):
        """"Initialization method with size (no type/value verification).

        Args:
            size (int): The size of the square.

        """
        self.__size = size
