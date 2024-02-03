#!/usr/bin/python3

'''
Write a function that adds 2 integers.
1. Prototype: def add_integer(a, b=98):
2. a and b must be integers or floats, otherwise raise a
TypeError exception with the message a must be an
integer or b must be an integer
3. a and b must be first casted to integers if they are float
4. Returns an integer: the addition of a and b
5. You are not allowed to import any module

Below is the solution
'''


def add_integer(a, b=98):

    """ function that adds 2 integers """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return(int(a) + int(b))
