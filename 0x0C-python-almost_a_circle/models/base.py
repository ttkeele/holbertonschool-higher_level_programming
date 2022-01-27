#!/usr/bin/python3
"""module that contains base class"""


class Base:
    """base class"""
    __nb_objects = 0

    def __ini__(self, id=None):
        """initailizes object

        Arg:
            id(int): id to assign
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
