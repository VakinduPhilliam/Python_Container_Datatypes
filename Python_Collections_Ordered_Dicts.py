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
# OrderedDict objects:
# Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted.
# When iterating over an ordered dictionary, the items are returned in the order their keys were first added.
#

#
# class collections.OrderedDict([items]): 
# Return an instance of a dict subclass, supporting the usual dict methods.
# An OrderedDict is a dict that remembers the order that keys were first inserted.
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.
# Deleting an entry and reinserting it will move it to the end.
# 

#
# popitem(last=True): 
# The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
# The pairs are returned in LIFO order if last is true or FIFO order if false.
#
# move_to_end(key, last=True). 
# Move an existing key to either end of an ordered dictionary.
# The item is moved to the right end if last is true (the default) or to the beginning if last is false.
# Raises KeyError if the key does not exist:
# 

d = OrderedDict.fromkeys('abcde')

d.move_to_end('b')
''.join(d.keys())

# OUTPUT: 'acdeb'

d.move_to_end('b', last=False)
''.join(d.keys())

# OUTPUT: 'bacde'
