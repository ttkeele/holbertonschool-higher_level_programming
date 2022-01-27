#!/usr/bin/python3
"""module that contains rectangle class"""


from models.base import Base


class Rectangle(Base):
    """rectangle class inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initilizes the rectagle

        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            x: vertical location of rectangle
            y: horizontal location of rectangle
            id: id for rectangle
        """
