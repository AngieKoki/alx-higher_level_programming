#!/usr/bin/python3

#computes the square value of all integers of a matrix

def square_matrix_simple(matrix=[]):
    res=[]
    for item in matrix:
        res.append(list(map(lambda x: x**2, item)))
    return(res)
