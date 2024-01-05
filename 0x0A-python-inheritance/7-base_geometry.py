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
        raise Exception("area() is not implemented")

        def integer_validator(self, name, value):
            """
            Public instance method to validate the value.
            Args:
                Name: Asting representing the name of the value.
                Value: The value to be validated.
            """
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
