#!/usr/bin/python3

'''
Write a class Square that defines a square by: (based on 1-square.py)
1. Private instance attribute: size
2. Instantiation with optional size: def __init__(self, size=0):
3. size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
4. if size is less than 0, raise a ValueError exception
with the message size must be >= 0
5. You are not allowed to import any module
Below is the solution
'''


"""Defining a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initializing a new Square.

        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
