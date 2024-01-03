#!/usr/bin/python3
"""Defines a class-checking function"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is an instance of specified class or inherited class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns: True if obj is an instance of a_class or its subclasse,
        False otherwise.
    """
    return isinstance(obj, a_class)
