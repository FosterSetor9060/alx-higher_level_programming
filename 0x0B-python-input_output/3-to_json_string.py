#!/usr/bin/python3
"""Defining a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return ing the JSON representation of a string_object."""
    return json.dumps(my_obj)
