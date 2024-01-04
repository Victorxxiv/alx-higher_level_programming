#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Public instance method tat raises an exception method.
        """

        def integer_validator(self, name, value):
            """
            Public instance method to validate the value.
            Args:
                Self:
                Name:
                Value: The value to be validated.
            Returns:
            """
            if not isinstance(value, int):
                raise TypeError
