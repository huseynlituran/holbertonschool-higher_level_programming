#!/usr/bin/python3
"""
This module defines class MyList that inherits from list
and adds a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList class inheriting from list with a method print_sorted()
    """

    def print_sorted(self):
        """
        Prints the list but sorted in ascending order
        without modifying the original list
        """
        print(sorted(self))
