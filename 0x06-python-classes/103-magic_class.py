#!/usr/bin/python3

"""Defining a Magic_Class matching exactly a bytecode provided by ALX."""

import math


class MagicClass:
    """Representing a circle."""

    def __init__(self, radius=0):
        """Initializing a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returning The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
