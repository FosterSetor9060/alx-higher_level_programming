#!/usr/bin/python3
"""Defining a Python class-to-JSON function."""


def class_to_json(obj):
    """Returning dictionary represntation of simple data structure"""
    return obj.__dict__
