#Dictionary and Set

#Dictionary -> Dictionary are used to store data values in key:value pairs. They are unordered, mutable and dont allow duplicate keys.

dict = {
    "name" : "midhun",
    "age" : 30,
    "gender" : "male"
}

print(dict["name"])
print(dict["age"])
print(dict["gender"])

dict["name"] = "Bobby"
dict["surname"]= "sharma"
print(dict)

#Nested Dictionary
student = {
    "name" : "midhun",
    "subject" : {
        "python" : "starting",
        "javascript": "medium"
    }
}
print(student)
print(student["subject"])
print(student["subject"]["python"])

#Dictionary Methods
print(student.keys()) #-> to get all the keys
print(list(student.keys()))
print(len(student)) #-> to get length of dictionary
print(len(list(student.keys())))

print(student.values()) # -> to get all the values
print(list(student.values()))
print(student.items()) #-> return all the values in tuple
print(list(student.items()))
print(student.get("name")) #-> to get the value of the given key
student.update({"city":"indore"})
print(student)

#------------><----------------#
#Ste in Python -> Set is the collection of unordered items. Each elements in the set must be unique and immutable.
collection = {1, 2, 3, 4, "Hello", True}
print(len(collection))
print(type(collection))
#To create empty set
newSet = set()
print(type(newSet))
newSet.add("Midhun")
newSet.add(11)
print(newSet)
newSet.remove(11)
print(newSet)
newSet.clear() #-> clear the set
print(len(newSet))
newSet = {1, 2 , "My", "Name", "is", "Midhun", "Nair"}
#newSet.pop() #-> remove any random vlaue from the set.
print(newSet)

set1 = newSet.union(collection) # -> union returns a new set with all the unique value from both the sets
print(set1)

set2 = newSet.intersection(collection) # -> intersection returns a new set with common value from both the given sets
print(set2)

#Question 1 - Store following word meanings in a python dictionary
# table: "a piece of furniture", "list of facts & figure"
# cat: "a small animal"

myDict = {
    "table" : ["a piece of furniture", "list of facts & figure"],
    "cat" : "a small animal"
}
print(myDict)

#Question 2 - You are given a list of subject for students. assume one classroom is required for 1 subject. how many classrooms are needed by all the students.
# python, java, c++, python, javascript, java, python, java, c++, c

subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print(len(subjects))

#Question 3 - WAP to enter marks of three subjects from the user and store them in a dictionary. 

myDict1 = {}
math = int(input("Enter marks of Math: "))
myDict1.update({"Math" : math})
science = int (input("Enter marks of Science: "))
myDict1.update({"Science" : science})
hindi = int(input("Enter marks of Hindi: "))
myDict1.update({"Hindi" : hindi})
print(myDict1)

