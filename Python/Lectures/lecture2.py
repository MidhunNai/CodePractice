# Strings
str = "my name is Midhun Nair"
# To concanicate string use +
str1 = "Midhun"
str2 = "Nair"
name = str1 + " " + str2
# To count charecters including space and special char use len
print(len(name))

# To access charecter use indexing
print(name[0])

# String Functions
print(str.endswith("Nair")) # -> Check strings end with given value
str = str.capitalize() # -> capitalize() is used to capitalize 1st char and create new string
print(str)
print(str.replace("a", "o")) #-> To replace any string or charec with other value
print(str.find("i")) #-> To find any substring or chare and return index of that sunstring or char
print(str.count("i")) #-> To count the sunstring or char in the given string

# Question: Take name as input from usewr and print the length of name
#name = input("Enter your name: ")
#print("Length of name is: ", len(name))

# Question: Take input from user and print the number of occurence of an sub string 
#strg = input("Enter any sentance : ")
#value = input("Enter substring to find its no. of occurance : ")
#print("Occurance : ", strg.count(value))

# Conditional Statement
#if-elif-else statement
age = 24
if(age >= 18):
    print("Can Vote")
else:
    print("CANNOT vote")

mark = int(input("Enter student's mark: "))
if(mark >= 90):
    grade = "A"
elif(mark < 90 and mark >= 80):
    grade = "B"
elif(mark >= 70 and mark < 80):
    grade = "C"
else:
    grade = "D"
print("Grade of student is: ", grade)

#------------------------#
#Question 1 -> WAP to check if a number entered by the user is odd or even
num = int(input("Enter any number:"))
if(num%2 == 0):
    print("Given number is even.")
else:
    print("Given number is odd")
#Question 2 -> WPA to find the greatest of 3 numbers entered by the user
num1 = int(input("Enter any first number:"))
num2 = int(input("Enter any second number:"))
num3 = int(input("Enter any third number:"))
greatest = 0
if(num1 > num2 and num1 > num3):
    greatest = num1
elif(num2 > num3):
    greatest = num2
else:
    greatest = num3
print(greatest)
#Question 3 -> WAP to check if a enteredde number is multiple of 7 or not
num4 = int(input("Enter number: "))
if(num4 % 7 == 0):
    print("Given number is multiple of 7")
else:
    print("Given number is not a multiple of 7")