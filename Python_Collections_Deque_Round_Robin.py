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
# A round-robin scheduler can be implemented with input iterators stored in a deque.
# Values are yielded from the active iterator in position zero.
# If that iterator is exhausted, it can be removed with popleft(); otherwise, it can be cycled back to the end with the rotate() method:
# 

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"

    iterators = deque(map(iter, iterables))

    while iterators:

        try:
            while True:
                yield next(iterators[0])

                iterators.rotate(-1)

        except StopIteration:

            # Remove an exhausted iterator.

            iterators.popleft()
