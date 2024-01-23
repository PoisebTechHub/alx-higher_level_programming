#!/usr/bin/python3

'''
Writing a function that raises a name exception with a message.
1. Prototype: def raise_exception_msg(message=""):
2. You are not allowed to import any module
Below is the solution
'''


def raise_exception_msg(message=""):
    """Raise a NameError exception with a message."""
    raise NameError(message)
