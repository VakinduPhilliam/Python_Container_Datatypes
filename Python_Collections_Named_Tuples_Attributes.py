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
# In addition to the methods inherited from tuples, named tuples support three additional methods and two attributes.
# To prevent conflicts with field names, the method and attribute names start with an underscore.
#

#
# classmethod somenamedtuple._make(iterable): 
# Class method that makes a new instance from an existing sequence or iterable.
# 

t = [11, 22]

Point._make(t)

# OUTPUT: 'Point(x=11, y=22)'

#
# somenamedtuple._asdict(): 
# Return a new OrderedDict which maps field names to their corresponding values:
# 

p = Point(x=11, y=22)

p._asdict()

# OUTPUT: 'OrderedDict([('x', 11), ('y', 22)])'
 
#
# somenamedtuple._replace(**kwargs): 
# Return a new instance of the named tuple replacing specified fields with new values:
# 

p = Point(x=11, y=22)

p._replace(x=33)

# OUTPUT: 'Point(x=33, y=22)'

for partnum, record in inventory.items():

           inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())

#
# somenamedtuple._fields: 
# Tuple of strings listing the field names.
# Useful for introspection and for creating new named tuple types from existing named tuples.
# 

p._fields            # view the field names

# OUTPUT: '('x', 'y')'

Color = namedtuple('Color', 'red green blue')

Pixel = namedtuple('Pixel', Point._fields + Color._fields)
Pixel(11, 22, 128, 255, 0)

# OUTPUT: 'Pixel(x=11, y=22, red=128, green=255, blue=0)'

#
# somenamedtuple._fields_defaults 
# Dictionary mapping field names to default values.
# 

Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
Account._fields_defaults

# OUTPUT: '{'balance': 0}'

Account('premium')

# OUTPUT: 'Account(type='premium', balance=0)'
 
#
# To retrieve a field whose name is stored in a string, use the getattr() function:
# 

getattr(p, 'x')

# OUTPUT: '11'
 
#
# To convert a dictionary to a named tuple, use the double-star-operator:
# 

d = {'x': 11, 'y': 22}

Point(**d)

# OUTPUT: 'Point(x=11, y=22)'
