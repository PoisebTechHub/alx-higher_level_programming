#!/usr/bin/python3

"""
Write a class MyList that inherits from list:

1. Public instance method: def print_sorted(self):
that prints the list, but sorted (ascending sort)
2. You can assume that all the elements of the list
will be of type int
3. You are not allowed to import any module

Below is the solution
"""


class MyList(list):
    """ List contains elements of type int """

    def print_sorted(self):
        """ Prints the list in ascending order """
        print(sorted(self))
