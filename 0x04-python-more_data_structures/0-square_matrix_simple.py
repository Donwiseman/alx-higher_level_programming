#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    new_m = [[x**2 for x in row] for row in matrix]
    return new_m
