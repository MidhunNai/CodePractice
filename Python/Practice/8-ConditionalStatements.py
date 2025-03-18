# Conditional Statements

# if elif else statements

"""
Syntax
if condition:
    do this
elif condition:
    do this
else condition:
    do this
"""

# 1. Positive, Negative, or Zero
# num = int(input("Enter any number : "))
# if (num < 0):
#     print("Negative Number!")
# elif (num == 0):
#     print("Zero!")
# else:
#     print("Positive Number")

# 2. Even or Odd Checker
# num = int(input("Enter any number : "))
# if(num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

# 3. Leap year checker
# num = int(input("Enter any year : "))
# if(num % 400 == 0):
#     print("Leap Year!")
# elif(num % 4 == 0 and num % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year!")

# 4. Grading System
marks = int(input("Enter your marks : "))
if(marks >= 90):
    print("A Grade")
elif(marks >= 80 and marks <= 89):
    print("B Grade")
elif(marks >= 70 and marks <= 79):
    print("C Grade")
elif(marks >= 60 and marks <= 99):
    print("D Grade")
else:
    print("F")
