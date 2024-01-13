#!/usr/bin/python3

'''Write a function that computes the square value
of all integers of a matrix using map'''


def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))
