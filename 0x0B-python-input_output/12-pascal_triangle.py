#!/usr/bin/python3

"""D
Technical interview preparation:

1. You are not allowed to google anything
2. Whiteboard first
3. Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:

4. Returns an empty list if n <= 0
5. You can assume n will be always an integer
6. You are not allowed to import any module

Below is the solution
"""


def pascal_triangle(n):
    """Representing Pascal's Triangle of size n.

    Returning a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
