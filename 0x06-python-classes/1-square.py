#!/usr/bin/python3

'''
Write a class Square that defines a square by: (based on 0-square.py)
1. Private instance attribute: size
2. Instantiation with size (no type/value verification)
3. You are not allowed to import any module
Below is the solution
'''


"""Defining class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size):
        """Initializing a new Square.

        Args:
            size (int): Size of the new square.
        """
        self.__size = size
