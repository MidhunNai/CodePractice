# Functions in Python

"""
A function is a block of reusable code that performs a specific task. Functions are used to organize code, improve readability, and promote reusability.

Types of functions in Python
1. Built-in function - print(), len, max()
2. User-defined function - function we create
3. Lambda Functions - Anonymous (one-liner) functions
"""
# Defining a Function - use def function_name() :
def print_hello():
    print("Hello World!")

print_hello()

# Function with parameter
def greet(name): # name is parameter
    print(f"Hello {name}!")

greet("Midhun") # Midhun is argument which will go in parameter name

# Function with multiple parameter
def calculate_sum(a, b, c):
    print(a + b + c)

calculate_sum(1, 1, 1)

# Default value of parameter if ser does not pass value
def hello_user(name = "User"):
    print(f"Hello {name}!")
hello_user("Midhun") # Hello Midhun!
hello_user() # Hello User!

# Keyword arguments (Named arguments)
def get_diff(a, b):
    print(a - b)
get_diff(a = 10, b = 15)
get_diff(b = 15, a = 10)

# *args (Multiple arguments)
"""
1. Used when you want to pass multiple values as arguments
2. Collects arguments as a tuple
"""

def calculate_sum(*numbers):
    total = sum(numbers)
    print(f"Total of given number is {total}.")
calculate_sum(1, 2, 4, 5, 6)
nums = (1, 2, 3, 4, 5)
calculate_sum(*nums)

def print_names(*names):
    for i in names:
        print(i)
print_names("Midhun", "Vimi", "Molly", "Vijayan")
friends = ["Durgesh", "Bobby", "Pankaj", "Dev"]
print_names(*friends)

def greet_user(greet, *users):
    for i in users:
        print(f"{greet} {i}!")
greet_user("Welcome", "Midhun", "Vimi", "Molly", "Vijayan")
greet_user("Hello", *friends)

# **kwargs - Keyword Variable-Length Arguments
"""
**kwargs in Python allows you to pass a variable number of keyword arguments (arguments with key-value pairs) to a function.
Syntax
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value})
"""

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
user ={
    "Name": "Midhun",
    "Age" : 30,
    "Working": True
}
user_info(**user)

def order_summery(customer_name, *items, **details):
    print(f"Customer : {customer_name}")
    for item in items:
        print(f"Item : {item}")
    print("Order Details :")
    for key, value in details.items():
        print(f"{key} : {value}")

order_items = ["Burger", "Pizza", "Soda"]
order_details = {
    "Waiting Time" : "30 Mins",
    "Total Bill" : "Rs 500"
}
order_summery("Midhun", *order_items, **order_details)

counter = 0
def add_to_counter():
    global counter
    new_number = int(input("Enter number to add : "))
    counter += new_number
    print(counter)
add_to_counter()