#!/usr/bin/python3
"""
creates class inheriting from the list class
"""


class MyList(list):
    """class MyList inherits from list"""

    def print_sorted(self):
        """prints the list"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
