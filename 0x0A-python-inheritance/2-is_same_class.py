#!/usr/bin/python3
"""
function that returns True if object is an instance the class

"""


def is_same_class(obj, a_class):
    """function that returns True if object is an instance the class"""

    if type(obj) is not a_class:
        return False

    return True
