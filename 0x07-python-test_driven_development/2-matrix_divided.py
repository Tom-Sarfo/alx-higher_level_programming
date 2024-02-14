#!/usr/bin/python3


"""This module is made up of a function that divides all elements of a matrix
   Args:
       matrix: this is the matrix whose element is to be divided.
       dvd (int, float): this is the divisor of the matrix.
"""


def matrix_divided(matrix, dvd):
    """This function divides all the elements of a matrix.
       Returns: A new list of matrix for which the elements have been divided.
    """

    new_matrix = [[]]

    # check for valid matrix format.

    type_err = "matrix must be a matrix (list of lists) of integers/float"

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(type_err)

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(type_err)

    # check for valid lenght of rows.
    first_row_len = len(matrix[0])

    for row in matrix:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(dvd, (int, float)):
        raise TypeError("dvd must be a number")

    if dvd == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round((x / dvd), 2) for x in row] for row in matrix]

    return (new_matrix)
