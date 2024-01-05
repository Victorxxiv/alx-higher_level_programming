#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Rectangle class, inherits from BaseGeomtry."""

    def __init__(self, width, height):
        """
        Intializes a Rectangle instance.
        Args:
            Width: width of the rectangle(positive integer).
            Height: Height of the rectangle (positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height",height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string represntation of the Rectangle.
        return: String representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
