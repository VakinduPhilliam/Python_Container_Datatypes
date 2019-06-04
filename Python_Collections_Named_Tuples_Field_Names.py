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
# Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3 modules:
# 

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv

for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

import sqlite3

conn = sqlite3.connect('/companydata')

cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')

for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)
