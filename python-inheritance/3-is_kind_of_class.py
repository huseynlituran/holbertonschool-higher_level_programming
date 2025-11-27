#!/usr/bin/python3
"""Check if object is an instance of, or inherited from, a class"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or inherited from it.

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        True if obj is instance of a_class or its subclass, False otherwise
    """
    return isinstance(obj, a_class)
