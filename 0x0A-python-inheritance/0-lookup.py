#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    return: A list containing the names of attributes and methods.
    """
    return dir(obj)
