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
# Counter objects
# A counter tool is provided to support convenient and rapid tallies.
#

#
# For example:
# 

# Tally occurrences of words in a list

cnt = Counter()

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        cnt[word] += 1

cnt

# OUTPUT: 'Counter({'blue': 3, 'red': 2, 'green': 1})'

# Find the ten most common words in Hamlet

import re

words = re.findall(r'\w+', open('hamlet.txt').read().lower())

Counter(words).most_common(10)
