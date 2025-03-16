# Python Tuples 
"""
A tuple is an immutable, ordered collection in Python that can hold multiple items. Like lists, tuples can store different data types, but once created, its values cannot be changed (immutable).

Tuple Characteristics
✅ Ordered → Elements maintain their defined order.
✅ Immutable → Elements cannot be changed, added, or removed.
✅ Heterogeneous → Can store multiple data types.
✅ Faster than lists → Tuples are optimized for performance.
✅ Hashable → Can be used as keys in dictionaries (if they contain only immutable elements).
"""

#Creating tuple
myTuple1 = (1, 2, 3, "Midhun", True) #With parenthesis
myTuple2 = 4, 5, 6, "Nair", False
singleTuple = (5,) #for single valued tuple comma is mandatory

#Accessing tuple values - use index

fruits = ("Apple", "Banana", "Pineapple")
print(fruits[0])
print(fruits[2])

#Tuple methods

#count() - Returned number of occurrence of specified value
print(fruits.count("Apple"))

#index() - returned the first index of specified value
print(fruits.index("Banana"))

#Tuple operations

#Concatenation
a = (1, 2) + (3, 4)
print(a) #(1, 2, 3, 4)

# Repetition
b = ("Hi", ) * 3
print(b) # ("Hi", "Hi", "Hi")

# Slicing - Removing values
c = (1, 2, 3, 4, 5)[1:4]
print(c)

#Length - len()
print(len(c))

# Membership Test
print("apple" in ("apple", "orange")) # True

# Unpacking Tuple - we can assign tuple values to variable in one go
person = ("Midhun", 30, )

# 1. Create a tuple of 5 numbers. Use .count() and .index() on the tuple.
newTuple = (9, 8, 7, 6, 5)
print(newTuple.count(7))
print(newTuple.index(9))

# 2. Write a program to swap two variables using tuple unpacking.
a = 5
b = 6
(a, b) = (b , a)
print(a , b)