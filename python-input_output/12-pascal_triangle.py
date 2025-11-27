#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)

    return triangle
