#!/usr/bin/python3
"""Defines the class Square"""


class Square:
    """Represents the square"""

    def __init__(self, size=0):
        """Initializes new square

        Args:
            size (int): Size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns current area of the square"""
        return (self.__size * self.__size)
