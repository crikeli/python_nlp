# Sorting.

x = [4,1,2,3]
y = sorted(x)
# Returns a brand new list
print y

# original x remains intact
print x

x.sort()
# Now x is sorted
print x

# Reverse Sorting by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key = abs, reverse = True)
print x

# Transforming a list into another list by choosing certain elements (List Comprehensions)

# Returns even numbers between 0 & 5
even_numbers = [x for x in range(5) if x % 2 == 0]
print even_numbers
# Returns square nums between 0 & 6
squares = [x*x for x in range(6)]
print squares
# Makes use of an existing list(even_numbers) and returns squares of them.
even_squares = [x*x for x in even_numbers]
print even_squares

# Lists can also be turned to dictionries or Sets
square_dict = {x : x*x for x in range(5)}
print square_dict

square_set = {x*x for x in [1,-1]}
print square_set

pairs = [(x,y)
        for x in range(10)
        for y in range(10)]
print pairs
