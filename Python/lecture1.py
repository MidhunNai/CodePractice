# Print Statement print()
print("String - Midhun")
print("Boolean - True/False")
print("Float - 11.25")
print("Integer - 1 , -1 , 0")
print("None")
# Print sum of two number
a = 5
b = 5
sum = a + b
print(sum)
# Types of operators
"""
Arithematic Operators (+, -, *, /, %, **)
Relational/Comparision Operators (==, !=, >, <, >=, <=)
Assignment Operators (= , += ,-+ ,/=, %=, **=)
Logical Operators (not, and, or)
"""
# To check type -> use type(value)
# Type Conversion : Python will automatically do type conversion
# Type casting : Muanually converting type of variable.
"""
To cast into int -> int(value)
To cast into float -> float(value)
To cast into string -> str(value)
"""

# To take input from user
"""
input("Enter your name: ")
"""
name = input("Enter your name: ")
print("Welcome, ", name)

# Write program to input 2 number and print their sum.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sum = number1 + number2
print("Sum of given numbers is: ", sum)

# Write a program to input side of square and print the area
side = float(input("Enter side of square: "))
print("Area of square is: ", side * side)