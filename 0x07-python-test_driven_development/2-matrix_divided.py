#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines  matrix division function"""


def matrix_divided(matrix, div):
    """Divides elements of the matrix

    Args:
        matrix (list): List of lists of ints or floats
        div (int/float): Divisor
    Raises:
        TypeError: if the matrix contains non-numb
        TypeError: if the matrix contains rows of diff sizes
        TypeError: if div is not an int or a float
        ZeroDivisionError: if div is 0
    Returns:
        new matrix representing the result of the division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
