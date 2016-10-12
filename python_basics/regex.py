# Regular expressions

import re

print all ([
    # Returns true because cat does not start with a
    not re.match("a", "cat"),

    # Returns true because cat has a in it
    re.search("a", "cat"),

    # Returns true because there is no c in dog
    not re.search("c", "dog"),

    # Returns true because the length is 3 after splitting a or b
    3 == len(re.split("[ab]", "carbs")),

    # Returns R-D- because the digits are substituted by dashes.
    "R-D-" == re.sub("[0-9]","-", "R2D2")
])
