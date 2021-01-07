#!/usr/bin/python3
""" Module doc """


def matrix_divided(matrix, div):
    """ divides all elments of a matrix """
    mat = matrix[:]
    for i in range(len(matrix)):
        size = len(matrix[0])
        if size != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float,int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    mat = [[round(x/div, 2) for x in mat[i]] for i in range(len(mat))] 
    return mat
