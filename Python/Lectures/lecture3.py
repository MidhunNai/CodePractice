#List and Tuple

#List -> A built in data type that stores set of values it is similar to Array

marks = [11.1, 12.1, 13.1, 14.0, 15.2] # -> this is list, we can store element of diff data type
print(marks)
print(type(marks))
print(marks[1])
print(len(marks))
student = ["Midhun", 25, "Thrissur"]
print(student)
# Strings are immutable where as list are mutable
student[0] = "Bobby"
print(student)
#Slicing
#listName[startingIndex, endingIbdex] -> create new list, inculde startingIndex but does not include endingIndex

#List Methods
marks.append(45.3) #-> add element at the end of list
print(marks)
marks.sort() #-> By defauld sorting ascending order
print(marks)
marks.sort(reverse=True) #-> Sort in descending order
print(marks)
char = ['a', 'b', 'c', 'd']
char.reverse() # -> Reverse the list
print(char)
marks.insert(3, 67.11) # -> Insert new element at any index
print(marks)
marks.remove(45.3) # -> Remove any elemnet first occurrence of element
print(marks)
marks.pop(1) # -> Remove the value at perticular index
print(marks)

#Tuple - A build in data type that lets us create immuatable sequence of values

tup = (2, 1, 3)
print(type(tup))
print(tup[0])
tup1 = () #-> create empty tuple
tup2 = (1,) # -> always create tuple of single value with comma
print(tup.index(1)) #-> Get element at given index
print(tup.count(2)) #-> Get count of given element in the tuple

# Question 1 -> WAP to ask user to enter names of 3 movies and store them in a list
movie1 = input("Enter 1st movie: ")
movie2 = input("Enter 2nd movie: ")
movie3 = input("Enter 3dr movie: ")
movieList = [movie1, movie2, movie3]
print(movieList)

# Question 2 -> WAP to check if the list is palindrome
list1 = [1, 2, 3, 2, 1]
list2 = list1.copy()
list2.reverse()
print(list2)
if(list1 == list2):
    print("Given list is palindrome")
else:
    print("Given list is not an palindrome")

# Question 3 -> WAP to count the number of student with A grade in the following tuple ('C', 'D', 'A', 'A', 'B', 'B', 'A')

newTup = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
print(newTup.count("A"))

newList = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
print(newList)
newList.sort()
print(newList)