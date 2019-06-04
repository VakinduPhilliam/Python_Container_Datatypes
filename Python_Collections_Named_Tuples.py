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
# namedtuple() Factory Function for Tuples with Named Fields
# 
# Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.
# They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
#
# collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
# Returns a new tuple subclass named typename.
# The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable.
# Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in
# a name=value format.
#

# 
# The field_names are a sequence of strings such as ['x', 'y'].
# Alternatively, field_names can be a single string with each fieldname separated by whitespace and/or commas, for example 'x y' or 'x, y'.
#

# Basic example

Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)     # instantiate with positional or keyword arguments

p[0] + p[1]             # indexable like the plain tuple (11, 22)

# OUTPUT: '33'

x, y = p                # unpack like a regular tuple
x, y

# OUTPUT: '(11, 22)'

p.x + p.y               # fields also accessible by name

# OUTPUT: '33'

p                       # readable __repr__ with a name=value style

# OUTPUT: 'Point(x=11, y=22)'
