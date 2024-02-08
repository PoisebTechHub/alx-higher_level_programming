#!/usr/bin/python3

"""
Write a class BaseGeometry (based on 5-base_geometry.py).

1. Public instance method: def area(self): that raises an Exception
with the message area() is not implemented
2. You are not allowed to import any module

"""


class BaseGeometry:
    """ This class is of geometry """
    def area(self):
        """ gathers area of a shape """
        raise Exception("area() is not implemented")
