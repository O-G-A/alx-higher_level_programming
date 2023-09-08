#!/usr/bin/python3
# 4-print_square.py
"""Defines square-printing function"""


def print_square(size):
    """Prints square with the # character

    Args:
        size (int): Height/width of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
