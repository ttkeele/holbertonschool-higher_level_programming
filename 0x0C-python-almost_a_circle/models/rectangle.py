#!/usr/bin/python3
"""
Contains the "Rectangle" class
"""

from models.base import Base


class Rectangle(Base):
    """A representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

     @property
     def width(self):
         """getter of width"""
         return self.__width

     @property
     def height(self):
         """getter of height"""
         return self.__height

     @property
     def x(self):
         """getter of x"""
         return self.__x

     @property
     def y(self):
         """getter of y"""
         return self.__y
