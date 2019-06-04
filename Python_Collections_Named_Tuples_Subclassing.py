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
# Subclassing is not useful for adding new, stored fields.
# Instead, simply create a new named tuple type from the _fields attribute:
# 

Point3D = namedtuple('Point3D', Point._fields + ('z',))

# 
# Docstrings can be customized by making direct assignments to the __doc__ fields:
# 

Book = namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'

Book.id.__doc__ = '13-digit ISBN'

Book.title.__doc__ = 'Title of first printing'

Book.authors.__doc__ = 'List of authors sorted by last name'
 
#
# Default values can be implemented by using _replace() to customize a prototype instance:
# 

Account = namedtuple('Account', 'owner balance transaction_count')

default_account = Account('<owner name>', 0.0, 0)
johns_account = default_account._replace(owner='John')

janes_account = default_account._replace(owner='Jane')
