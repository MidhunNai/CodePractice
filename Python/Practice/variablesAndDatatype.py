#Variables in python

#We can directly define variable without giving data type
name = "Midhun"
age = 30
isWorking = True

#Data Types
"""
String
Integer
Float
Boolean
List
Dictionary
Tuple
Set
"""

name = "Vimi" #Data type String str
age = 33 #Data type integer int
isWorking = True #Datatype boolean bool
pi = 3.14 #Data type float
fruits = ["Apple", "Banana", "Mango"] #Data type list
tupleEx = (1, 2, 3, 4) #Data type tuple
dictionaryEx = {"name": "Midhun"} #Data type Dictionary dict
setEx = {1, 2, 4, 5} #Data type set

#Type Checking
print(type(name))
print(type(age))
print(type(isWorking))
print(type(pi))
print(type(fruits))
print(type(tupleEx))
print(type(dictionaryEx))
print(type(setEx))

#Type conversion
"""
int() -> to convert into integer
float() -> to convert into float
str() -> to convert into string
bool() -> to convert into boolean
"""
print("----------------")
num = 10
print(type(num))
num = float(num)
print(type(num))
num = str(num)
print(type(num))
num = bool(num)
print(type(num))
print(num)

# 1. Ask the user for their name and print a greeting like: Hello, [Name]! Welcome to Python programming.

userName = input("Enter you name : ")
print(f"Hello, {userName}! Welcome to Python programming.")

# 2. Create a program that stores the following information in variables and prints it in a sentence: 1. Your name 2. Your favorite color 3. Your birth year

userData = {}
userData['name'] = input("Enter your name : ")
userData['favColor'] = input("Enter your fav color : ")
userData['birthYear'] = int(input("Enter your birth year : "))
print(f"Your name is {userData['name']}, your fav color is {userData['favColor']} and you born in {userData['birthYear']}")
