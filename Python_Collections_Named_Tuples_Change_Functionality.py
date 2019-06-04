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
# Since a named tuple is a regular Python class, it is easy to add or change functionality with a subclass.
#
# Here is how to add a calculated field and a fixed-width print format:
# 

class Point(namedtuple('Point', ['x', 'y'])):

        __slots__ = ()

        @property

        def hypot(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

        def __str__(self):
            return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Point(3, 4), Point(14, 5/7):

        print(p)

# OUTPUT: 'Point: x= 3.000  y= 4.000  hypot= 5.000'
# OUTPUT: 'Point: x=14.000  y= 0.714  hypot=14.018'
