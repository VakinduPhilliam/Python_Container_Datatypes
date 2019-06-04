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
# Another approach to using deques is to maintain a sequence of recently added elements by appending to the right and popping to the left:
# 

def moving_average(iterable, n=3):

    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average

    it = iter(iterable)

    d = deque(itertools.islice(it, n-1))

    d.appendleft(0)

    s = sum(d)

    for elem in it:
        s += elem - d.popleft()

        d.append(elem)

        yield s / n
