#!/usr/bin/python3
"""
This module defines the lookup function
which returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes
    and methods of an object.
    """
    return dir(obj)
