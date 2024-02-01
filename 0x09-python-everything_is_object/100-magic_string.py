#!/usr/bin/python3

'''
Write a function magic_string() that returns a string “BestSchool”
n times the number of the iteration (see code):
1. Format: see example
2. Your file should be maximum 4-line long (no documentation needed)
3. You are not allowed to import any module

Below is the solution
'''


def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
