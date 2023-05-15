#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
        return
    for row in matrix:
        for index, value in enumerate(row):
            if (index + 1) == len(row):
                print("{:d}".format(value))
                break
            print("{:d} ".format(value), end="")
