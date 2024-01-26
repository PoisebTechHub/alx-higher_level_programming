#!/usr/bin/python3

'''
Write a class Square that defines a square by: (based on 3-square.py)
1. Private instance attribute: size:
2. property def size(self): to retrieve it
3. property setter def size(self, value): to set it:
4. size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
5. if size is less than 0, raise a ValueError exception
with the message size must be >= 0
6. Instantiation with optional size: def __init__(self, size=0):
7. Public instance method: def area(self):
that returns the current square area
8. You are not allowed to import any module
Below is the solution
'''


"""Definition of class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int): Size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Geting or setting the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returning the current area of the square."""
        return (self.__size * self.__size)
