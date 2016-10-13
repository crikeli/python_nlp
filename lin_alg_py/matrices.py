# 2d collection of numbers.
# Matrices are represented as lists of lists

# 2X3 Matrix
# Each row is an n X k matrix with a vector length of k
# Each column is of length n
A = [[1,2,3],
     [4,5,6]]

# 3X2 Matrix
B = [[1,2],
     [3,4],
     [5,6]]

# 3X2 Matrix
C = [[1,2,4,5],
     [3,4,5,6],
     [5,6,4,3]]

# A snippet to get the dimension of a matrix
def shape(A):
    num_rows = len(A)
    num_columns = len(A[0]) if A else 0
    return num_rows, num_columns
print "This is a",shape(C), "matrix"

# Gets all values in a specified row of a matrix
def get_row(A,i):
    return A[i]
print get_row([[1,2,3],
              [4,5,6]], 0)

# Gets all values in a specified column of a matrix
def get_column(A,j):
    return [A_i[j] for A_i in A]
print get_column([[1,2,3],
                  [4,5,6]], 1)

# A function that creates matrices.
# Function takes in num_rows, num_cols and a function that works on the previous 2 vals
def make_matrix(num_rows, num_cols, entry_fn):
    # Execute the entry_fn for entire iterations of num_rows & num_cols
    return [[entry_fn(i,j)
        for i in range(num_rows)]
        for j in range(num_cols)]

def is_diagonal(i,j):
    # returns 1 if the value of i is the same as j.
    return 1 if i == j else 0

identify_matrix = make_matrix(2,2,is_diagonal)
print identify_matrix
