#!/usr/bin/python3

'''
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :

1. Prototype: def text_indentation(text):
2. text must be a string, otherwise raise a TypeError
exception with the message text must be a string
3. There should be no space at the beginning or
at the end of each printed line
4. You are not allowed to import any module

Below is the solution
'''


def text_indentation(text):
    """ function that prints 2 new lines """

    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")

    for a in range(len(text)):
        for b in range(len(text)):
            if b == size - 1:
                print("#")
            else:
                print("", end="")
