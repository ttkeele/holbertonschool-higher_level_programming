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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
