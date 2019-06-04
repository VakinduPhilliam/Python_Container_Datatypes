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
# Example patterns for using the ChainMap class to simulate nested contexts:
# 

c = ChainMap()        # Create root context
d = c.new_child()     # Create nested child context

e = c.new_child()     # Child of c, independent from d
e.maps[0]             # Current context dictionary -- like Python's locals()

e.maps[-1]            # Root context -- like Python's globals()
e.parents             # Enclosing context chain -- like Python's nonlocals

d['x']                # Get first key in the chain of contexts
d['x'] = 1            # Set value in current context

del d['x']            # Delete from current context

list(d)               # All nested values

k in d                # Check all nested values

len(d)                # Number of nested values

d.items()             # All nested items

dict(d)               # Flatten into a regular dictionary
