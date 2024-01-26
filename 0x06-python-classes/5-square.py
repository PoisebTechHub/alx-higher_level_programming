#!/usr/bin/python3

'''
Write a class Square that defines a square by: (based on 4-square.py)
1. Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
if size is less than 0, raise a ValueError
exception with the message size must be >= 0
2. Instantiation with optional size: def __init__(self, size=0):
3. Public instance method: def area(self):
that returns the current square area
4. Public instance method: def my_print(self):
that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
5. You are not allowed to import any module
Below is the solution
'''


"""Defining  a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size):
        """Initializing a new square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getting or setting the current size of the square."""
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

    def my_print(self):
        """Printing the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
