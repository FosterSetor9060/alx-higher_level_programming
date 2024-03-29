#!/usr/bin/python3

"""Defining a class Square."""


class Square:
    """Representinh a square."""

    def __init__(self, size=0):
        """Initialize a new_Square.

        Args:
            size (int): The size of the new_square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
