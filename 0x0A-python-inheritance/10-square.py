#!/usr/bin/python3
"""module contains class Square"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """class is a square that inherits rectangle"""

    def __init__(self, size):
        """initilizes the square

        Arg:
            size(int): length of square's sides
        """
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns area of the square"""
        return super().area()
