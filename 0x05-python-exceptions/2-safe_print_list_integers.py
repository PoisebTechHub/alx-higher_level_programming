#!/usr/bin/python3

'''
Writing a function that prints the first x elements
of a list and only integers.
1. Prototype: def safe_print_list_integers(my_list=[], x=0):
2. my_list can contain any type (integer, string, etc.)
3. All integers have to be printed on the same line followed
by a new line - other type of value in the list must
be skipped (in silence).
4. x represents the number of elements to access in my_list
5. x can be bigger than the length of my_list - if it’s the case,
an exception is expected to occur
6. Returns the real number of integers printed
7. You have to use try: / except:
8. You have to use "{:d}".format() to print an integer
9. You are not allowed to import any module
10. You are not allowed to use len()
Below is the solution
'''


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return (count)
