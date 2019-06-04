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
# More Counter Objects
#

#
# elements() 
# Return an iterator over elements repeating each as many times as its count.
# Elements are returned in arbitrary order.
# If an element’s count is less than one, elements() will ignore it.
# 

c = Counter(a=4, b=2, c=0, d=-2)

sorted(c.elements())

# OUTPUT: '['a', 'a', 'a', 'a', 'b', 'b']'

#
# most_common([n]) 
# Return a list of the n most common elements and their counts from the most common to the least.
# If n is omitted or None, most_common() returns all elements in the counter.
# Elements with equal counts are ordered arbitrarily:
# 

Counter('abracadabra').most_common(3)  # doctest: +SKIP

# OUTPUT: '[('a', 5), ('r', 2), ('b', 2)]'

#
# subtract([iterable-or-mapping]): 
# Elements are subtracted from an iterable or from another mapping (or counter).
# Like dict.update() but subtracts counts instead of replacing them.
# Both inputs and outputs may be zero or negative.
# 

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)

c.subtract(d)
c

# OUTPUT: 'Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})'
 
#
# The usual dictionary methods are available for Counter objects except for two which work differently for counters.
#

#
# fromkeys(iterable) 
# This class method is not implemented for Counter objects.
#
# update([iterable-or-mapping]) 
# Elements are counted from an iterable or added-in from another mapping (or counter).
#
# Like dict.update() but adds counts instead of replacing them.
# Also, the iterable is expected to be a sequence of elements, not a sequence of (key, value) pairs.
#

# 
# Common patterns for working with Counter objects:
# 

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts

list(c)                         # list unique elements
set(c)                          # convert to a set

dict(c)                         # convert to a regular dictionary

c.items()                       # convert to a list of (elem, cnt) pairs

Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs

c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts

# 
# Several mathematical operations are provided for combining Counter objects to produce multisets (counters that have counts greater than zero).
# Addition and subtraction combine counters by adding or subtracting the counts of corresponding elements.
# Intersection and union return the minimum and maximum of corresponding counts.
# Each operation can accept inputs with signed counts, but the output will exclude results with counts of zero or less.
# 

c = Counter(a=3, b=1)

d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]

# OUTPUT: 'Counter({'a': 4, 'b': 3})'

c - d                       # subtract (keeping only positive counts)

# OUTPUT: 'Counter({'a': 2})'

c & d                       # intersection:  min(c[x], d[x]) # doctest: +SKIP

# OUTPUT: 'Counter({'a': 1, 'b': 1})'

c | d                       # union:  max(c[x], d[x])

# OUTPUT: 'Counter({'a': 3, 'b': 2})'
 
#
# Unary addition and subtraction are shortcuts for adding an empty counter or subtracting from an empty counter.
# 

c = Counter(a=2, b=-4)
+c

# OUTPUT: 'Counter({'a': 2})'

-c

# OUTPUT: 'Counter({'b': 4})'


#
# To enumerate all distinct multisets of a given size over a given set of elements
# 

map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC
 