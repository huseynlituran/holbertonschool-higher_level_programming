#!/usr/bin/python3
"""
This module contains a function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends to  text and returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
