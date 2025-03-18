"""Loops in Python
Loops are used to repeat a block of code multiple times. Python provides two primary types of loops:
	1.	for loop — Used for iterating over sequences like lists, strings, etc.
	2.	while loop — Runs as long as a specified condition is True.
"""
# for Loops

"""
Syntax
for variable in sequence:
    code to execute
"""

fruits = ["apple", "banana", "orange"] # for loop in list
for fruit in fruits:  # fruit is variable for individual elements of fruits sequence
    print(fruit)

# range() - generally used to iterate for number
for i in range(10):
    print(i)

"""
range(start, stop, step)
	•	start → Starting value (default is 0)
	•	stop → The loop stops before this value
	•	step → The increment (default is 1)
"""
for i in range(2, 10, 2):
    print(i)

name = "midhun"
revName = []
for char in name:
    revName.append(char)
revName.reverse()
result = "".join(revName)
print(result)

"""
while loop
while condition:
    code to execute
"""

count = 1
while count <= 5:
    print(count)
    count += 1