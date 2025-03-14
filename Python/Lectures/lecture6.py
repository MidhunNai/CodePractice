#Functions -> Block of statement that perform a specifi task
"""
Python function syntax
def functionName(params):
    block of code
    return value
"""
#Function to calculate sum of two number
def calculateSum(a, b):
    sum = a + b
    print(sum)
    return sum

calculateSum(10,10)

#Function to calculate average of three number
def cal_avg(a, b, c):
    return (a+b+c)/3

print(cal_avg(3,3,3))

#Type of function in Python -> Build In and User defined 
#Default Parameter
def cal_product(a = 2, b =2): #Default value should be in last
    print(a * b)
    return a * b

cal_product()

#Question 1 -> WAP to print the length of a list. (list in the parameter)
def cal_len(myList):
    return len(myList)

myList = [2, 4, 6, 8]
cal_len(myList)
#Question 2 -> WAP tp print the element of a list in a single line (list in parameter)
def print_ele(myList):
    for ele in myList:
        print(ele, end=" ")

print_ele(myList)

#Question 3 -> WAP to fid the factorial of n (n in paramete)
def cal_factorial(n):
    i = n
    factorial = 1
    while i > 0:
        factorial *= i
        i -= 1
    print(factorial)
    return factorial

cal_factorial(5)

#Question 4 -> WAP to convert USD to INR
def convert_usd(usd):
    return usd * 81
print(convert_usd(5))

#Question 5 -> WAF to find odd and even number
def check_oddeven(n):
    if(n % 2 == 0):
        print("Even")
    else:
        print("Odd")

check_oddeven(83)

#Recursion -> When a function calls itself repeatedly
"""
Syntax
def functionName(param):
    condition: #if()
        return
    functionName(param) # calling itself
"""
#Print all the number till n using recursion
def printNum(n):
    if(n == 0):
        return
    print(n)
    printNum(n-1)

printNum(10)

#Find factorial of num using recursion
def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1) * n

print(fact(5))

#Question 1 -> Write a recursive function to calculate the sum of first n natualr numbers.

def find_sum(n):
    if(n == 0):
        return 0
    return find_sum(n-1) + n

find_sum(5)

#Question 2 -> Write a recursive function to print all the element in a list

yourList = [1, 21, 32, 43, 54]

def print_List(list, index = 0):
    if(index == len(list)):
        return
    print(list[index])
    print_List(list, index+1)

print_List(yourList)