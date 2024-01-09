#!/usr/bin/python3

# Write a function that prints a matrix of integers
def print_matrix_integer(matrix=[[]]):   # Prototype given
    for row in matrix:   # Defining row in matrix
        for column in row:  # Defininf column in matrix
            print("{:d}".format(column), end=" " if column != row[-1] else "")
        print()
