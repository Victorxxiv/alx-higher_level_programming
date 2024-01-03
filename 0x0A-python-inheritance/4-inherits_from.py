#!/usr/bin/python3
"""Defines a fuction that checks the origin of an object"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of inherited or specific class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Return: True if obj is an instance of a class that inherited from a_class,
        False otherwise.
    """
    return issubclass(type(obj), a_class)
