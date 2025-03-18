# Loop Questions

# 1. Write a Python program to print numbers from 1 to 10 using a while loop.
# num = 1
# while(num <= 10):
#     print(num)
#     num += 1

# 2. Create a program that prints all even numbers between 1 and 20 using a for loop.   
# for i in range(1, 21):
#     if(i % 2 == 0):
#         print(i) 

# 3. Write a Python program that asks the user for numbers until they enter 0. Then print the sum of all entered numbers.
# num = int(input("Enter any number : "))
# sum = 0
# while(num != 0):
#     sum += num
#     num = int(input("Enter number again : "))
# print("Sum of all entered number is ", sum)

# 4. Use a for loop to print the multiplication table of 5.
# for i in range(1, 11):
#     print(f"5 * {i} = {5 * i}")

# 5. Create a countdown timer from 10 to 1 using a while loop, then print "Time's up!".
# time = 10
# while(time > 0):
#     print(time)
#     time -= 1
# print("Time's up!")

# 6. Write a program that prints the square of each number from 1 to 10.
# for i in range(1, 11):
#     print(i * i)

# 7. Write a Python program that prints all numbers divisible by 3 between 1 and 50.
# for i in range(1, 51):
#     if(i % 3 == 0):
#         print(i)

# 8. Write a Python program to find the sum of the first 10 natural numbers.
# n = int(input("Enter any number : "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

# 9. Write a program that asks the user for 5 numbers and prints their average.
# sum = 0
# for i in range(1, 6):
#     num = int(input(f"Enter any number {i} : "))
#     sum += num 
# print(sum/5)

# 10. Write a Python program that prints the factorial of a given number.
# num = int(input("Enter any number to calculate its factorial : "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(factorial)

# 11. Create a program that prints the Fibonacci series up to n terms.
# n = int(input("Enter any number : "))
# a = 0
# b = 1
# sum = 0
# result = [a, b]
# for i in range(1, n - 2):
#     sum = a + b
#     result.append(sum)
#     a = b
#     b = sum
# print(result)

# 12. Write a Python program that counts how many times the letter 'a' appears in a given string.
# str = "aaaa bbbb aaaa"
# count = 0
# for a in str:
#     if(a == "a"):
#         count += 1
# print(count)

# 13. Write a Python program to print the following number pattern:
"""
1
12
123
1234
12345
"""
# for i in range(1, 6):
#     for j in range (1, i+1):
#         print(j,end="")
#     print()

# 14. Print the following pattern:
"""
*
**
***
****
*****
"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# 15. Create a program that prints the multiplication table from 1 to 5 using nested loops.

# for i in range(1, 6):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")

# 16. Print the following pattern:
"""
*****
****
***
**
*
"""
# star = 5
# for i in range(1, 6):
#     for j in range(1, star + 1):
#         print("*", end="")
#     star -= 1
#     print()

# 17. Print the following pattern:
"""
**********
 ********
  ******
   ****
    **
     *
"""

# rows = 6
# for i in range(rows):
#     print(" " * i + "*" * (2 * (rows - i) - 1))

# 15. Write a Python program to print this pattern:
"""
A
BB
CCC
DDDD
"""
# rows = 5
# for i in range(rows):
#     print(chr(64 + i) * i)

# 16. Write a Python program to find the largest and smallest number in a list without using built-in functions like max() or min().

# myList = [8, 10, 20, 3, 71, 0, 11]

# largest = float('-inf')
# smallest = float('+inf')
# for i in myList:
#     if(largest < i):
#         largest = i
#     if(smallest > i):
#         smallest = i
# print(largest, smallest)
# print(max(myList))
# print(min(myList))

# 17. Create a program that asks the user for numbers until they enter -1, then print the total sum.
# num = int(input("Enter any number : "))
# sum = 0
# while(num != -1):
#     sum += num
#     num = int(input("Enter number again : "))
# print("Sum of all entered number is ", sum)

# 18. Write a program that prints the reverse of a given number.
# num = 11081994
# numStr = str(num)
# revNum = ''.join(reversed(numStr))
# result = int(revNum)
# print(result)

# 19. Write a Python program that checks whether a number is palindrome or not.
# myString = "Midhun"
# myString = myString.lower()
# rev = "".join(reversed(myString))
# if(myString == rev):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 20. Create a number guessing game where the program randomly picks a number, and the user must guess it. Give hints like "Too high" or "Too low".
# import random

# secret_number = random.randint(1, 10)
# print(secret_number)
# user_number = int(input("Guess the number between 1 to 10 : "))
# attempts = 1
# while(secret_number != user_number):
#     attempts += 1
#     user_number = int(input("Guess the number again: "))
# print(f"The number was {secret_number} and you guessed it in {attempts} attempts")

# 21. Write a Python program that prints all the common elements between two lists.
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [5, 6, 7, 8, 9, 0]
# common_elements = list(set(list1).intersection(set(list2)))
# print(common_elements)

# 22. Write a program that counts the number of vowels in a given string.
# user_string = input("Enter any word to calculate number of vowel in it : ")
# user_string = user_string.lower()
# vowel_count = 0

# for i in user_string:
#     if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
#         vowel_count += 1
# print(f"There are {vowel_count} number of vowels in the given string")