#!/usr/bin/python3

"""
Write a function that reads a text file (UTF8)
and prints it to stdout:
1. Prototype: def read_file(filename=""):
2. You must use the with statement
3. You don’t need to manage file permission
or file doesn't exist exceptions.
4. You are not allowed to import any module

Below is the solution
"""


def read_file(filename=""):
    """Printing the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
