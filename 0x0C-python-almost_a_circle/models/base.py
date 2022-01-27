#!/usr/bin/python3
"""module that contains base class"""


class Base:
    """base class"""
    __nb_objects = 0

    def __ini__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
