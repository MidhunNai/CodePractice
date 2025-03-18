# Logical Operators
"""
 Logical operators are used to combine multiple conditions (boolean expressions) in Python. These operators return True or False based on the conditions.

 and - return true when both conditions are true
 or - return true when any one condition is true
 not - reverse the boolean value
"""
# 1. Write a Python program that checks if a number is between 10 and 20 using logical operators.
# num = int(input("Enter any number : "))
# if(num >= 10 and num <= 20):
#     print("Correct number")
# else:
#     print("Enter number between 10 and 20")

# 2. Create a program that verifies if a given year is a leap year using logical operators.
# year = int(input("Enter any year : "))
# if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
#     print("Leap Year!")
# else:
#     print("Not a Leap Year!")

# 3. Write a Python program that asks for a user’s age and country, and prints if they are eligible to vote (Assuming voting age is 18+)
age = int(input("Enter your age : "))
country = input("Enter your country : ").lower()
if(age >= 18 and (country == "india" or country == "usa")):
    print("Eligible for vote!")
else:
    print("Data not available for this country.")