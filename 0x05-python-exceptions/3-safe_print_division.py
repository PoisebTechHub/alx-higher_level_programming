#!/usr/bin/python3

'''
Writing a function that divides 2 integers and prints the result.
1. Prototype: def safe_print_division(a, b):
2. You can assume that a and b are integers
3. The result of the division should print on the finally:
section preceded by Inside result:
4. Returns the value of the division, otherwise: None
5. You have to use try: / except: / finally:
6. You have to use "{}".format() to print the result
7. You are not allowed to import any module
Below is the solution
'''


def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
