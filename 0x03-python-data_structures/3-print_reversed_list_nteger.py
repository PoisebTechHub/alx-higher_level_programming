#!/usrr/bin/python3
# Write a function that prints all integers of a list in reverse order

def print_reversed_list_integer(my_list=[]):   # Prototype given
    if isinstance(my_list, list):
        my_list.reverse()
        for k in my_list:
            print("{:d}".format(k))
