#!/usr/bin/python3
"""Divide a matrix module"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix

    Args:
        matrix: a list of lists of integers or floats.
        div: a number (integer or float) to divide by.

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats.
        TypeError: Each row of the matrix must have the same size.
        TypeError: div must be a number.
        ZeroDivisionError: if div is 0.

    Returns:
        A new matrix with the divided elements.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
