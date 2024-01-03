#!/usr/bin/python3
"""Defines Class MyList that inherits from list"""


class MyList(list):
    """MyList inherits from the built-in list class"""

    def print_sorted(self):
        """Prints the list in sorted in ascending order"""
        print(sorted(self))
