#Loops

"""
while Loop - syntax
while condition:
    do this
"""
#Print hello 5 times
count = 1
while count <= 5:
    print("Hello")
    count += 1
#Print number from 1 to 100
i = 1
while i<=100:
    print(i)
    i += 1
#Print number from 100 to 1
i = 100
while i > 0:
    print(i)
    i -= 1
#print the multipilcation table of a number n
#n = int(input("Enter any number:"))
n = 5
i = 1
while i <= 10:
    print(n*i)
    i += 1
#Print the element of the following list using a loop
list = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(list):
    print(list[i])
    i += 1
#Search for a number x in the above tuple
tup = (1,4,9,16,25,36,49,64,81,100)
i = 0
n = 81
while i < len(tup):
    print(i)
    if tup[i] == n:
        print("Found")
        break
    i += 1

#break is used to terminate loop
#continue is used to skip current itteration

#For Loop
"""
Syntax
for el in list:
    do this
"""
#Print all element in list
veggie = ["tomato", "potato", "capsicum", "cucumber", "pumpkin"]
for element in veggie:
    print(element)

#Print the element of thr following list using loop: 
myList = [1,4,9,16,25,36,49,64,81,100]
for ele in myList:
    print(ele)

#Search for a number in the given tuple
k = 49
mytup = (1,4,9,16,25,36,49,64,81,100)
for ele in mytup:
    if(ele == n):
        print("Found")
    else:
        print("Finding...")
else:
    print(k, "found")

#range() -> Range function returns a sequence of number, starting from 0 by default, and increments by 1(by default), and stops before a specified number, does not include the specified number. range(5) -> 0, 1, 2, 3, 4
#range(start?, stop, step?)

for i in range(10): #range(stop)
    print(i)

for i in range(2, 10): #range(start, stop)
    print(i)

for i in range(2, 10, 2): #range(start, stop, step)
    print(i)

#pass Statement -> pass is a null statement that does nothing. It is used as placeholder for future code
for el in range(10):
    pass

#Question : WAP to find the sum of first n number (using while)
n = int(input("Enter any number : "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(sum)

#Question : WAP to find the factorial of first n number (using for)
m = int(input("Enter a number to find its factorial :"))
factorial = 1
for el in range(m, 0, -1):
    factorial = factorial * el
print(factorial)