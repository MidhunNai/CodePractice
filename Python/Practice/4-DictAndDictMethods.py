#Python Dictionary Explained

"""A dictionary in Python is an unordered collection of key-value pairs. Unlike lists, which are indexed by position, dictionaries are indexed by keys.

✅ Key-Value Pairs → Each key is unique and maps to a value.
✅ Mutable → Values can be changed after creation.
✅ Unordered (Before Python 3.7) → Python 3.7+ maintains insertion order.
✅ Fast Lookups → Dictionaries are optimized for retrieving data."
"""
#Creating dictionary
myDict = {
    "name" : "Midhun",
    "age" : 30,
    "isWorking" : True
}
# Accessing value by dic["key"]
print(myDict["name"])
print(myDict["age"])
print(myDict["isWorking"])

#Common Dictionary Methods

# keys() - return all the keys in dictionary
print(myDict.keys())

# values() - return all the values from dictionary
print(myDict.values())

# items() - return key-value pair as tuple
print(myDict.items())

# get() - return the value of the key, if not found return default value
print(myDict.get("name", "not found"))
print(myDict.get("city", "not found"))

# update() - Update the dictionary with key-value pair
myDict.update({"age": 29})
print(myDict)

# pop() - remove the item with specified key and return its value
print(myDict.pop("age"))
print(myDict)

# popitem() - remove and return the last inserted key-value pair
print(myDict.popitem())
print(myDict)

# setdefault() - return the value of key, if key does not exist insert the key with specified value
print(myDict.setdefault("name", "India"))
print(myDict.setdefault("country", "India"))
print(myDict)

# copy() - return a shallow copy of dictionary
newDict = myDict.copy()
print(newDict)

# clear() - remove all the items from dictionary
newDict.clear()
print(newDict)