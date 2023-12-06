#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Class that defines a rectangle.

    Attritubes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialization method with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Rectangle height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
