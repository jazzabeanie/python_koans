#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    if (a<=0 or b<=0 or c<=0):
        raise TriangleError, "Triangles must have sides of length greater than zero, silly"
    elif ((a+b)<c or (b+c)<a or (a+c)<b):
        raise TriangleError, "Your triangle is physically impossible to construct without having one side curved"
    elif (a == b == c):
        return 'equilateral'
    elif ((a == b != c) or (b == c != a) or (a == c != b)):
        return 'isosceles'
    #had to comment out the following code to make it work. How do I do this?? Ideally I want to say if (any variable != int or float)
    #elif (any(type(a)!=int, type(b)!=int, type(c)!=int)):
    #    raise self.TriangleError
    else:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
