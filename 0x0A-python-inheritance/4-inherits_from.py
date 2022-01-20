#!/usr/bin/python3
"""
finds if object is an instance of a class that inherited
(directly or indirectly) from specified class
"""


def inherits_from(obj, a_class):
    """
    determines if obj is an instance of a class that
    inherited from a_class

    Args:
        obj: object to check
        a_class: class to check

    Returns: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
