#!/usr/bin/python3
"""
creates rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class for rectangles"""
    def __init__(self, width, height):
        """initilizes the width and height for the rectangle

        Args:
            width(int): width of Rectangle
            height(int): height of Rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """returns string representation of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
