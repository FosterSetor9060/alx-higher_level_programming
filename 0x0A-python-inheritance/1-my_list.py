#!/usr/bin/python3
"""Defining an inherited list class_MyList."""


class MyList(list):
    """Implementing sorted printing for the built-in list class."""

    def print_sorted(self):
        """Printing the list in sorted ascending order."""
        print(sorted(self))
