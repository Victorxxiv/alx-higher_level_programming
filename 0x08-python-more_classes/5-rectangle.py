#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Class that defines a rectangle.

    Attributes:
        width(int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializing Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height Getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".joint(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method to print a message when an instance is deleted."""
        print("Bye rectangle...")
