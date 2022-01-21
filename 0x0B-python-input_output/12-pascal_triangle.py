#!/usr/bin/python3
"""module that creates pascals triangle as a list"""


def pascal_triangle(n):
    """returns a list of integers representing
    pascals triangle
    """
    triangle = []
    for x in range(n):
        triangle.append([])
        for y in range(x + 1):
            if y == 0 or y == x:
                triangle[x].append(1)
            else:
                triangle[x].append(triangle[x - 1][y - 1] + triangle[x - 1][y])
    return triangle
