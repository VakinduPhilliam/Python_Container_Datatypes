# Python Collections
# collections — Container datatypes.
# This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
#
# namedtuple(): factory function for creating tuple subclasses with named fields.
# deque: list-like container with fast appends and pops on either end.
# ChainMap: dict-like class for creating a single view of multiple mappings.
# Counter: dict subclass for counting hashable objects.
# OrderedDict: dict subclass that remembers the order entries were added.
# Defaultdict: dict subclass that calls a factory function to supply missing values.
# UserDict: wrapper around dictionary objects for easier dict subclassing.
# UserList: wrapper around list objects for easier list subclassing.
# UserString: wrapper around string objects for easier string subclassing.
#

#
# OrderedDict: 
# Since an ordered dictionary remembers its insertion order, it can be used in conjunction with sorting to make a sorted dictionary:
# 

# regular unsorted dictionary

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key

OrderedDict(sorted(d.items(), key=lambda t: t[0]))

# OUTPUT: 'OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])'

# dictionary sorted by value

OrderedDict(sorted(d.items(), key=lambda t: t[1]))

# OUTPUT: 'OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])'

# dictionary sorted by length of the key string

OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))

# OUTPUT: 'OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])'
