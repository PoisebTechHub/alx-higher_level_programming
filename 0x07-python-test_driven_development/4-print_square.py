#!/usr/bin/python3

'''
Write a function that prints a square with the character #.

1. Prototype: def print_square(size):
2. size is the size length of the square
3. size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
4. if size is less than 0, raise a ValueError exception
with the message size must be >= 0
5. if size is a float and is less than 0, raise a TypeError
exception with the message size must be an integer
6. You are not allowed to import any module

Below is the solution
'''


def print_square(size):
    """ function that prints a square """

    if not isinstance(size, int) or size is None:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for a in range(size):
        for b in range(size):
            if b == size - 1:
                print("#")
            else:
                print("", end="")
