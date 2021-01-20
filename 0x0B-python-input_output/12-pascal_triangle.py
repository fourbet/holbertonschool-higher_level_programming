#!/usr/bin/python3
""" project: Python - Input Output """


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascals triangle of n"""

    if n <= 0:
        return []

    res = [[1 for col in range(row + 1)]for row in range(n)]
    for row in range(n):
        for col in range(row + 1):
            if col >= 1 and col < row:
                res[row][col] = res[row - 1][col - 1] + res[row - 1][col]
    return res
