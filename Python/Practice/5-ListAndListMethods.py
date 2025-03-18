# List

"""
A list in Python is a collection that can store multiple values in a single variable. Lists are:

✅ Ordered → Elements have a defined sequence (index-based).
✅ Mutable → You can modify elements (add, remove, change).
✅ Allow Duplicates → The same value can appear multiple times.
✅ Can Store Different Data Types → Integers, strings, booleans, etc.
"""

myList = [11, "Midhun", 3.14, True, "Midhun"] #Creating list

# List Methods

#append() - Add an item to the end of the list
myList.append("Nair")
print(myList)

#insert() - Insert an item at specified position
myList.insert(0, "Hello") # 0 is index and Hello is element which we need to insert at 0 index
print(myList)

#extend() - Adds multiple item to the list at the end
myList.extend(["Molly", "Vimi", "Vijayan"])
print(myList)

# remove() - Removes the first occurrence of the item
myList.remove("Midhun")
print(myList)

# pop() - remove the item at the specified index, default is last item
myList.pop()
print(myList)
myList.pop(0)
print(myList)

# index() - return the index of element's first occurrence
print(myList.index("Nair"))

# count() - count total occurrence of element in the list
print(myList.count("Molly"))

# sort() - sort list in ascending order
numList = [10, 3, 9, 1, 6, 4]
numList.sort()
print(numList)

# reverse()  - sort the list in descending order
numList.reverse()
print(numList)

# copy() - return a shallow copy of the list
numListCopy = numList.copy()
print(numListCopy)

# clear() - remove all the elements from the list
numListCopy.clear()
print(numListCopy)

"""
	1.	Create a list of 5 numbers and:
	•	Add two more numbers using .append().
	•	Remove the first number.
	•	Sort the list in descending order.
"""
newList = [11, 8, 1994, 13, 3]
newList.append(18)
newList.append(12)
print(newList)
newList.pop(0)
newList.sort()
print(newList)

"""
Create a list of your 3 favorite movies and:
	•	Insert a new movie at position 2.
	•	Reverse the list order.
	•	Print the index of your favorite movie.
"""
favMovies = ["movie1", "movie2", "movie3"]
favMovies.insert(1, "newMovie")
print(favMovies)
favMovies.reverse()
print(favMovies)
print(favMovies.index("newMovie"))
