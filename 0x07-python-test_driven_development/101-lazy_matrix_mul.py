#!/usr/bin/python3
""" Module doc """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplies  matrices by using the module NumPy """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in range(len(m_a)):
        if type((m_a[i])) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in range(len(m_b)):
        if type((m_b[i])) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            if not isinstance(m_a[i][j], (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in range(len(m_b)):
        for j in range(len(m_b[i])):
            if not isinstance(m_b[i][j], (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_a)):
        size_a = len(m_a[0])
        if len(m_a[i]) != size_a:
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        size_b = len(m_b[0])
        if len(m_b[i]) != size_b:
            raise TypeError("each row of m_b must be of the same size")
    row_b = len(m_b)
    column_a = len(m_a[0])
    if row_b != column_a:
        raise ValueError("m_a and m_b can't be multiplied")
    res = np.dot(m_a, m_b)
    return res
