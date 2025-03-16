# Basic printing question

# 1. Write a python program to print "Hello, World!"

print("Hello World!")

# 2. Print your name and age on separate lines
print("Midhun\n30")

# 3. print the following text exactly
"""
Python is fun!
Let's learn python together.
"""
print("Python is fun!\nLet's learn python together.")

#String concatenation

# 1. Write a program that asks user for their name and print
"""name = input("Enter your name:")
print("Welcome,", name)"""

# 2. Create two variables: firstName and lastName, then print them in the format
"""
First Name: <firstName>
Last Name: <lastName
"""
"""firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
print("First Name :", firstName, "\nLast Name :", lastName)"""

#3. Ask the user for two numbers and print their sum, difference, product, and quotient.
"""a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("Sum of given two number is ", a + b)
print("Difference for given number is ", a - b)
print("Product of given number is ", a * b)
if b != 0:
    print("Quotient of given two number is ", a / b)
else:
    print("Division by zero is not allowed")"""

# 4. Print Python's "print()" function is awesome!
print("Python's \"print()\" is awesome!")
print("To escape any \" we need to use \ before \"")

# 5. Print the following patter using \n and \t
"""
Name: John Doe
Age:   25
City:  New York
"""
print("Name:\tJohn Doe\nAge:\t25\nCity:\tNew York")

# 6. Print "The price is $50" using f-strings.
price = "$50"
print(f"The price is {price}")

# 7. Print "Today is Monday, and the temperature is 25°C" using .format().
today = "Monday"
temp = "25°C"
print(f"Today is {today} and the temperature is {temp}")

# 8. sep and end in print() - separator and ending
"""
Print
Apple | Banana | Cherry %
1-2-3-4-5 %
Task Complete! %
"""
print("Apple", "Banana", "Cherry", sep=" | ", end=" %\n")
print(1,2,3,4,5, sep="-", end=" %\n")
print("Task Complete!", end=" %\n")

# 9. Print the following text in one line using end parameter: Python is amazing!
print("Python", end=" ")
print("is", end=" ")
print("amazing!", end=" ")
