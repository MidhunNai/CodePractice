#Object Oriented Programmin OOPs

"""
To map with real world scenarios, we started using objects in code.
Class is a blueprint for creating object.
class Student():
    neam : "Midhun

Adding constructor 
class Student():
    def __init__(self, fullName):
        self.name = fullName
        print("constructor executed")
    name: "Midhun"

Creating object
s1 = Student("Midhun")
print(s1.name)

Class consist of Attributes and Method
Attribute : All the variables/data in class and object are called attributes, attribute defined in class are called class attribute. If we declare name using contructor then the variable is declared for object and that is called object attribute.

Methods : function defined in class are called method
class Students():
    def __init__(self, age): #age is an object attribute
        print("This is an constructor")
    name : "Midhun" #This is an class attribute

    def welcome(self):
        print("This is an method called welcome")


"""
class Students():
    def __init__(self, age, marks): #age is an object attribute
        self.marks = marks
        print("This is an constructor and object attribute is:", age)
    name = "Midhun" #This is an class attribute

    def welcome(self):
        print("This is an method called welcome")
    
    def get_marks(self):
        return self.marks

s1 = Students(30, 99)
s1.welcome()
print(s1.get_marks())

#Question 1: Create student class that takes name & marks of 3 subjects as argument in constructor. Then create a method to print the average.

class CollegeStudents():
    def __init__(self, name, physics, chemestry, math):
        self.name = name
        self.physics = physics
        self.chemestry = chemestry
        self.math = math
    
    def cal_average(self):
        return (self.physics + self.chemestry + self.math)/3
    
student1 = CollegeStudents("Midhun", 80, 70, 90)
print(student1.cal_average())
student2 = CollegeStudents("Bobby", 90, 80, 70)
print(student2.cal_average())

#Static Methods - Those method which does not need self parameter, it can only be created at class level.
"""
@staticmethod
def methodName():
    do this
"""

#Abstraction : Hiding the implementation details of a class and only showing the essendtial features to the user 
#Encapsulation : Wrapping data and function into a single unit (object)