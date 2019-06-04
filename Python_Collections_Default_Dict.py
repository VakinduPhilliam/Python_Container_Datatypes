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
# defaultdict:
# Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists:
# 

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for k, v in s:
        d[k].append(v)

sorted(d.items())

# OUTPUT: '[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]'
 
#
# When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the default_factory function
# which returns an empty list.
# The list.append() operation then attaches the value to the new list.
# When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation adds another value to the
# list.
# This technique is simpler and faster than an equivalent technique using dict.setdefault():
# 

d = {}

for k, v in s:
        d.setdefault(k, []).append(v)

sorted(d.items())

# OUTPUT: '[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]'

# 
# Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other languages):
# 

s = 'mississippi'
d = defaultdict(int)

for k in s:
        d[k] += 1

sorted(d.items())

# OUTPUT: '[('i', 4), ('m', 1), ('p', 2), ('s', 4)]'

# 
# When a letter is first encountered, it is missing from the mapping, so the default_factory function calls int() to supply a default count of zero.
# The increment operation then builds up the count for each letter.
#

# 
# The function int() which always returns zero is just a special case of constant functions.
# A faster and more flexible way to create constant functions is to use a lambda function which can supply any constant value (not just zero):
# 

def constant_factory(value):
        return lambda: value

d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
'%(name)s %(action)s to %(object)s' % d

# OUTPUT: 'John ran to <missing>'
 
#
# Setting the default_factory to set makes the defaultdict useful for building a dictionary of sets:
# 

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]

d = defaultdict(set)

for k, v in s:
        d[k].add(v)

sorted(d.items())

# OUTPUT: '[('blue', {2, 4}), ('red', {1, 3})]'
 