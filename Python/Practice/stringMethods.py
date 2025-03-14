#Common String Methods

# 1. upper() - Convert all character to upper case
text = "midhun"
print(text.upper())

# 2. lower() - convert all character to lower case
text = "MIDHUN"
print(text.lower())

# 3. title() - convert to title case
text = "my name is midhun nair"
print(text.title())

# 4. capitalize() - to capitalize first letter of the string
text = "hello world"
print(text.capitalize())

"""5. strip() - remove leading and ending spaces
      lstrip() - remove leading spaces
      rstrip() - remove ending spaces
"""
text = "   Python   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# 6. replace() - to replace any character with other character
text = "Hello World!"
print(text.replace(" ", "#"))

# 7. find() - to find first occurrence of substring and return its index
text = "Midhun Nair"
print(text.find("Na"))

# 8. count() - count how many times an substring appears 
text = "Midhun Midhun Midhun Vimi Molly"
print(text.count("m"))

# 9. startswith() and endswith() - to check given string starts and ends with the asked substring
text = "My name is Midhun Nair"
print(text.startswith("My"))
print(text.endswith("R"))

# 10. split() - split the given string in to list based on the delimiter (given separator)

text = "Hello world I like python"
myList = text.split(" ")
print(myList)

# 11. join() - join the list in to string based on the provided separator
text = "$".join(myList)
print(text)

# 12. len() - to get the length of string
text = "Midhun"
print(len(text))

# Reverse a string
revList = reversed(text)
revString = "".join(revList)
print(revString)