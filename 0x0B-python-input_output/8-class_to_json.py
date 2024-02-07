#!/usr/bin/python3
"""Defining all Python class-to-JSON function."""

def class_to_json(obj):
    """Returning all  the dictionary represntation of a simple data_structure."""
    return obj.__dict__
