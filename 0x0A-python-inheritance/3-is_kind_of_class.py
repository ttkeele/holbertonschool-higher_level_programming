#!/usr/bin/python3
"""
function that returns True if the object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
returns true or false

    Args:
        obj: object to look at
        a_class: class to evaluate

    Returns: True or False
    """

    return isinstance(obj, a_class)
