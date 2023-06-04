#!/usr/bin/python3
""" This module contains a function that divides all elements of a matrix

    Doctest for this function is carried out in tests/2-matrix_divided.txt

"""


def matrix_divided(matrix, div):
    """ divides all element of a matrix by a given divisor and returns it

    Args:
        matrix (list): A list conatining a list of ints or floats
        div (float or int): number to be used to divide through matrix

    Returns:
        list: returns a new matrix of elements from dividing matrix by div

    Raises:
        TypeError: if matrix contains a non int or float element and if
            individual rows are not of same length
        ZeroDivisionError: if divisor is zero

    """
    new_matrix = []

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers\
/floats")
    size = len(matrix[0])
    for m_list in matrix:
        if type(m_list) != list or not m_list:
            raise TypeError("matrix must be a matrix (list of lists) of int\
egers/floats")
        if size != len(m_list):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for value in m_list:
            if type(value) != int and type(value) != float:
                raise TypeError("matrix must be a matrix (list of lists) of i\
ntegers/floats")
            new_list.append(round(value / div, 2))
        new_matrix.append(new_list)
    return new_matrix
