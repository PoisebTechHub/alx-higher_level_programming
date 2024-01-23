#!/usr/bin/python3

'''
Writing the Python function def magic_calculation(a, b):
that does exactly the same as the following Python bytecode:
Below is the solution
'''


def magic_calculation(a, b):   # prototype of function
    result = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / k
        except Exception:
            result = b + a
            break
    return (result)
