#!/usr/bin/python3

"""
Write a function that writes a string to a text file (UTF8)
and returns the number of characters written:

1. Prototype: def write_file(filename="", text=""):
2. You must use the with statement
3. You don’t need to manage file permission exceptions.
4. Your function should create the file if doesn’t exist.
5. Your function should overwrite the content of the file
if it already exists.
6. You are not allowed to import any module

Below is the solution
"""


def write_file(filename="", text=""):
    """Writting a string to a UTF8 text file.

    Args:
        filename (str): Name of the file to write.
        text (str): Text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
