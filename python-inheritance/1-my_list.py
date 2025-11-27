#!/usr/bin/python3
"""
This module defines a MyList class that inherits from list
and provides a public method print_sorted that prints
the list in ascending order without modifying the list.
"""


class MyList(list):
    """
    MyList inherits from built-in list.
    """

    def print_sorted(self):
        """
        Print the list but sorted (ascending) without
        modifying the original list.
        """
        print(sorted(self))
