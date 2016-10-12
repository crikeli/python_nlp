# Enumerations for when I need to iterate over a list and use both, the element & the idx

#
# EXAMPLES BELOW
#

# for i, document in enumerate(documents):
#     do_something(i, document)
#
# # For only working with indices
#
# for i, _ in enumerate(documents):
#     do_something(i)

# Zipping Lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
result = zip(list1,list2)
print result

# Unzipping Lists
pairs = [('a', 1), ('b', 2), ('c', 3)]
# The asterisk performs argument unpacking
# It uses individual elements of "pairs" to perform zip
letters, numbers = zip(*pairs)
print letters,numbers

# Args & Kwargs (Arguments & Keyword Arguments)

# BOTTOM eg. Works
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)
print g(3)
print g(-1)

#  Bottom eg. does not work because g takes exactly 1 argument, not 2.
def f2(x, y):
    return x+y

g = doubler(f2)
# print g(1,2)

# TO make it work, it is important to specify a fn that takes arbut args.
def magic(*args, **kwargs):
    # args is a tuple of unnamed aruments
    print "unnamed args:", args
    # kwargs is a dictionary of named arguments
    print "keyword args:", kwargs

magic(1,2, key="word", key2="word2")

# The reverse side of working with args & kwargs
def other_way(x,y,z):
    return x+y+z

x_y_list = [1,2]
z_dict = {"z": 3}
print other_way(*x_y_list, **z_dict)
