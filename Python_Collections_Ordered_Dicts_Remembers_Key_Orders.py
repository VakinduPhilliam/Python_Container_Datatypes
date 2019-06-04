# Python Collections
# collections � Container datatypes.
# This module implements specialized container datatypes providing alternatives to Python�s general purpose built-in containers, dict, list, set, and tuple.
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
# The new sorted dictionaries maintain their sort order when entries are deleted.
# But when new keys are added, the keys are appended to the end and the sort is not maintained.
# 

#
# It is also straight-forward to create an ordered dictionary variant that remembers the order the keys were last inserted.
# If a new entry overwrites an existing entry, the original insertion position is changed and moved to the end:
# 

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):

        if key in self:
            del self[key]

        OrderedDict.__setitem__(self, key, value)
