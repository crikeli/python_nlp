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


        s = Set([1,2,3])
        print s
        s.add(4)
        print s
        print s.contains(4)
        s.remove(3)
        print s
        print s.contains(3)
