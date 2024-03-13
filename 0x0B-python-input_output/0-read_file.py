#!/usr/bin/python3
"""Defining the text file-reading_function."""


def read_file(filename=""):
    """Printing _contents of a UTF8 text_file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
