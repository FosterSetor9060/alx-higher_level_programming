#!/usr/bin/python3
"""Defining the locked class."""


class LockedClass:
    """
    Preventing the user from instantiating new LockedClass_attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
