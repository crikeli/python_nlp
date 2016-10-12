# Vector Addition in Python
# Achieved by zipping vectors together and using list Comprehensions
from __future__ import division
from matplotlib import pyplot as plt
import math

def vector_add(v,w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]
# print vector_add((1,4,5),(3,7,8))

# Vector subtraction is similarly Achieved
def vector_subtraction(v,w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]
# print vector_subtraction((2,5,7), (7,9,0))

# Component-wise sum of a list of vectors
# def vector_sum(vectors):
#     result = vectors[0]
#     for vector in vectors[1:]:
#         result = vector_add(result, vector)
#         return result

# OR
def vector_sum(vectors):
    return reduce(vector_add, vectors)
# print vector_sum((1,2,3,4))


# SCALAR MULTIPLICTION (number & vector)
def scalar_mult(c,v):
    return [c * v_i for v_i in v]
# print scalar_mult(7,[1,2,3])

# Vector Mean (Same size)
def vec_mean(vectors):
    n = len(vectors)
    return scalar_mult(1/n, vector_sum(vectors))
# print vec_mean([1,2,3])

# DOT product (Sum of the Component-wise products)
def dot(v,w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))
# print dot([1,2,3,4], [5,6,7,8])

# Sum of Squares
def sum_of_squares(v):
    return dot(v,v)
# print sum_of_squares((2,4,6,8))

# Calculating the magnitude(length) of the vectors
def magnitude(v):
    return math.sqrt(sum_of_squares(v))
# print magnitude([2,4,6,8])

# Finally it is possible to compute the distance between 2 vectors
def squared_distance(v,w):
    return sum_of_squares(vector_subtraction(v,w))
# print squared_distance

def distance(v,w):
    # return math.sqrt(squared_distance(v,w))
    # OR
    return magnitude(vector_subtraction(v,w))
print distance([1,2,3,5],[6,7,8,9])
