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
# The ChainMap class only makes updates (writes and deletions) to the first mapping in the chain while lookups will search the full chain.
# However, if deep writes and deletions are desired, it is easy to make a subclass that updates keys found deeper in the chain:
# 

class DeepChainMap(ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'

    def __setitem__(self, key, value):

        for mapping in self.maps:

            if key in mapping:
                mapping[key] = value

                return

        self.maps[0][key] = value

    def __delitem__(self, key):

        for mapping in self.maps:

            if key in mapping:
                del mapping[key]

                return

        raise KeyError(key)

d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})

d['lion'] = 'orange'         # update an existing key two levels down
d['snake'] = 'red'           # new keys get added to the topmost dict

del d['elephant']            # remove an existing key one level down
d                            # display result

DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})
 