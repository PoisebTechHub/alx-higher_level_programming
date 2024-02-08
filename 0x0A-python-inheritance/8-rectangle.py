#!/usr/bin/python3

"""
Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py).

1. Instantiation with width and height: def __init__(self, width, height):
2. width and height must be private. No getter or setter
3. width and height must be positive integers, validated
by integer_validator

Below is the solution
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Applies geometry to Rectangles """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
