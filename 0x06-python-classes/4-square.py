#!/usr/bin/python3
"""Defines the class Square"""


class Square:
    """Represents square"""

    def __init__(self, size=0):
        """Initializes new square

        Args:
            size (int): Size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Gets or sets the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current area of the square"""
        return (self.__size * self.__size)