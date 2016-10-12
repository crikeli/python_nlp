from collections import defaultdict
from collections import Counter

# An empty list is produced
dd_list = defaultdict(list)

# dd_list now contains {2: [1]}
dd_list[2].append(1)
print dd_list

# Empty dictionary is produced
dd_dict = defaultdict(dict)

# {"Joel" : {"City" : "Seattle"}}
dd_dict["Joel"]["City"] = "Seattle"
print dd_dict

dd_pair = defaultdict(lambda: [0,0])
# {2: [0,1]}
dd_pair[2][0] = 1
print dd_pair

# Counter maps keys to counts.
{0:2,1:1,2:1}
c = Counter([0,1,2,0])
print c

# Sets are simply a collection of distince elements
s = set()
s.add(1)
print s
s.add(2)
print s
s.add(1)
print s

x = len(s)
print x
# Checks for a value in the set and returns a bool.
y = 2 in s
print y
z = 3 in s
print z
