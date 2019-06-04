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
# deque
# class collections.deque([iterable[, maxlen]]): 
# Returns a new deque object initialized left-to-right (using append()) with data from iterable.
# If iterable is not specified, the new deque is empty.
#

# 
# Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”).
# Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either
# direction.
# Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and
# insert(0, v) operations which change both the size and position of the underlying data representation.
#

#
# Example:
# 

from collections import deque

d = deque('ghi')                 # make a new deque with three items

for elem in d:                   # iterate over the deque's elements
        print(elem.upper())

#
# OUTPUT:
#
# G
# H
# I
#

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
d                                # show the representation of the deque

# OUTPUT: 'deque(['f', 'g', 'h', 'i', 'j'])'

d.pop()                          # return and remove the rightmost item

# OUTPUT: 'j'

d.popleft()                      # return and remove the leftmost item

# OUTPUT: 'f'

list(d)                          # list the contents of the deque

# OUTPUT: '['g', 'h', 'i']'

d[0]                             # peek at leftmost item

# OUTPUT: 'g'

d[-1]                            # peek at rightmost item

# OUTPUT: 'i'

list(reversed(d))                # list the contents of a deque in reverse

# OUTPUT: '['i', 'h', 'g']'

'h' in d                         # search the deque

# OUTPUT: 'True'

d.extend('jkl')                  # add multiple elements at once

d

# OUTPUT: 'deque(['g', 'h', 'i', 'j', 'k', 'l'])'

d.rotate(1)                      # right rotation

d

# OUTPUT: 'deque(['l', 'g', 'h', 'i', 'j', 'k'])'

d.rotate(-1)                     # left rotation

d

# OUTPUT: 'deque(['g', 'h', 'i', 'j', 'k', 'l'])'

deque(reversed(d))               # make a new deque in reverse order

# OUTPUT: 'deque(['l', 'k', 'j', 'i', 'h', 'g'])'

d.clear()                        # empty the deque

d.pop()                          # cannot pop from an empty deque

d.extendleft('abc')              # extendleft() reverses the input order

d

# OUTPUT: 'deque(['c', 'b', 'a'])'
