#!/usr/bin/python3
""" project: Python - Input Output """


def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascals triangle of n"""

    if n <= 0:
        return []

    triangle = [[1 for column in range(row + 1)]for row in range(n)]
    if n >= 3:
        for row in range(n):
            for column in range(row + 1):
                if column >= 1 and column < row:
                    triangle[row][column] = triangle[row - 1][column - 1] + triangle[row - 1][column] 
    return triangle
