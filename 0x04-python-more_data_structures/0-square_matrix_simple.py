#!/usr/bin/python3

# Write a function that computes the square value of all integers of a matrix

def square_matrix_simple(matrix=[]):  # Protoytpe of function
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])
    return squared
