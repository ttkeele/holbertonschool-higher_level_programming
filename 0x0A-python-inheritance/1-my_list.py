an empty class BaseGeometry#!/usr/bin/python3
"""
creates class inheriting from the list class
"""


class MyList(list):
    """class MyList inherits from list, sorted"""

    def print_sorted(self):
        """prints list in order"""
         print(sorted(self))
