#!/usrr/bin/python3

# Write a function that prints all integers of a list in reverse order
def print_reversed_list_integer(my_list=[]):   # Prototype given
    if my_list:
        for k in my_list[::-1]:   # The -1 ensures it starts from reverse
            print("{:d}".format(k))
