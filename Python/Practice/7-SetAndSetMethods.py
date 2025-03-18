# Python Sets Explained

"""
A set is an unordered, mutable, and unique collection in Python that does not allow duplicate values.

Key Characteristics of Sets
✅ Unordered → Elements are stored in random order (no indexing).
✅ Mutable → You can add or remove elements.
✅ Unique → Automatically removes duplicate values.
✅ Unindexed → Since sets are unordered, they cannot be accessed via indexes.
✅ Optimized for Membership Tests → Fastest way to check if an item exists in a collection.
"""

# Declaring Set
mySet = {1, 2, 3, 4, 5, 5, 6, 7, 7} # Duplicate will be removed
print(mySet)

newSet = set() # create and empty set
newSet2 = set([2, 5, 7, 1, 7, 8]) # We can give list in set() duplicate will be removed
print(newSet2)

# Set Methods

# add() - Adds an element to the set
exSet = set()
exSet.add(11)
print(exSet)

# update() - Adds multiple elements to the set
exSet.update([2, 1994])
print(exSet)

# remove() - remove an element, raise error when not found
exSet.remove(1994)
print(exSet)
#exSet.remove(1994)

# discard() - remove an element without error if not found
exSet.discard(1994)

# pop() - remove and return an random element
print(exSet.pop())

# copy() - create a shallow copy of set
exSet2 = exSet.copy()
print(exSet2)

# clear() - Empties the set
exSet2.clear()
print(exSet2)

# Set operations
a = {1, 2, 3}
b = {2, 3, 4, 5, 6}

# union() - combines both the set removes duplicate
print(a.union(b))
# intersection() - gives the common elements
print(a.intersection(b))
# difference() - gives all element of a not in b
print(a.difference(b))
# symmetric_difference() - Gives element unique in each set
print(a.symmetric_difference(b))
# issubset() - check if a is subset of b
c = {9, 8}
d = {9, 8, 7, 6}
print(c.issubset(d))
# issuperset() - checks if a is superset of b
print(c.issuperset(d))
print(d.issuperset(c))

# Member testing
fruits = {"apple", "banana", "orange"}
print("apple" in fruits)
print("cherry" in fruits)

# Frozen set - A frozen set is an immutable version of a set. Once created, you cannot modify its contents.
fSet = frozenset([1, 2, 3, 4, 5])
#fSet.add(9) - error
#fSet.remove(1) - error

# 1. Write a Python program that removes duplicates from a list using a set.
myList = [1, 1, 2, 3, 4, 4]
newSet3 = set(myList)
print(newSet3)
myList = list(newSet3)
print(myList)
