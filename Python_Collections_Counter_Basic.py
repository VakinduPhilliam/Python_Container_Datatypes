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
# class collections.Counter([iterable-or-mapping]): 
# A Counter is a dict subclass for counting hashable objects.
#

#
# It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
# Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
#

# 
# Elements are counted from an iterable or initialized from another mapping (or counter):
# 

c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable

c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
 
