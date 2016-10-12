# Object Oriented Programming in Python refresher

# Bellow is an annotated example of creating a class

class Set:

    # Below are functions of the class
    # Every function takes a "self" parameter
    # "self" refers to the particular Set object being used.

    # A constructor that gets called when a new Set is created
    # eg. s1 = Set() or s2 = Set([1,2,2,3])
    def __init__(self, values = None):

        # Each instance of a set has it's own dictionary property
        self.dict = {}

        if values is not None:
            for value in values:
                self.add(value)

        # This is a string representation of the Set object
        def __repr__(self):
            return "Set: " + str(self.dict.keys())

        # Membership is represented by being a key in self.dict with the value true
        def add(self, value):
            self.dict[value] = True

        # Value is in the set if it is a key in the dictionary
        def contains(self, value):
            return value in self.dict

        # The del property is used to remove a certain value
        def remove(self, value):
            del self.dict[value]

# Usage
# s = Set([1,2,3])
# print s
# s.add(4)
# print s
# print s.contains(4)
# s.remove(3)
# print s
# print s.contains(3)

from functools import partial

# Understanding map, reduce, filter

def double(x):
    return 2 * x

xs = [1,2,3,4]
twice_xs = [double(x) for x in xs]
print twice_xs

twice_xs = map(double, xs)
print twice_xs

# partial helps make a function of just one variable(first arg)
# partial can be used to fill later args by naming them

# map(function, iterable)
# list_doubler is a function that doubles a list
list_doubler = partial(map, double)
print list_doubler

twice_xs = list_doubler(xs)
print twice_xs

def multiply(x, y):
    return x*y
# MAP functionality
products = map(multiply, [1,2], [4,5])
print ("final_products-map:", products)

def is_even(x):
    # True if even(x%2==0), false if odd
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]
print ("x_evens", x_evens)

# Filter takes in 2 args, the function (is_even) and the iterable(xs)
# FILTER functionality
x_evens = filter(is_even, xs)
print ("x_evens:", x_evens)

list_evener = partial(filter, is_even)

x_evens = list_evener(xs)
print ("final_x_evens-filter:", x_evens)

# REDUCE functionality
x_product = reduce(multiply, xs)
print ("x_prod:", x_product)

list_product = partial(reduce, multiply)
print (list_product)

x_prodcut = list_product(xs)
print ("final_x_prod-reduce:", x_product)
