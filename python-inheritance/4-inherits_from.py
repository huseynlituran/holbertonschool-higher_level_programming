#!/usr/bin/python3
"""Check if object inherited from specified class (not the class itself)"""


def inherits_from(obj, a_class):
    """
    Return True if obj is instance of a class that inherited from a_class.
    Returns False if obj is an instance of a_class itself.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        True if obj inherited from a_class (but not a_class itself)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
