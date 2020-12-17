#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = matrix[:]
    for i in range(len(matrix)):
        new = list(map(lambda x: x * x, matrix[i]))
        new_mat[i] = new
    return (new_mat)
