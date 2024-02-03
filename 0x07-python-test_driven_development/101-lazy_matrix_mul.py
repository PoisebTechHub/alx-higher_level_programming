#!/usr/bin/python3

'''
Write a function that multiplies 2 matrices
by using the module NumPy

1. To install it: pip3 install numpy==1.15.0
2. Prototype: def lazy_matrix_mul(m_a, m_b):
3. Test cases should be the same as 100-matrix_mul
but with new exception type/message

Below is the solution
'''
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplying m_a and m_b using
    matmul, and returning the result
    """
    return numpy.matmul(m_a, m_b)
