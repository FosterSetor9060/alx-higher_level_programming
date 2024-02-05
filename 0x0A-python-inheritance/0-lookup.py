0-lookup.py
#!/usr/bin/python3
"""Defining an object attribute lookup_function."""


def lookup(obj):
    """Returning the list of an object's available attributes."""
    return (dir(obj))
