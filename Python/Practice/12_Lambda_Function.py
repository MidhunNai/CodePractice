# Lambda Function

"""
A lambda function is a small, anonymous function in Python. It’s defined using the lambda keyword and can have any number of arguments but only one expression.
Syntax

lambda arguments: expression
"""
# 1. Basic lambda function
from functools import reduce


add = lambda a, b: a + b # add is a variable which is reference to lambda function used ti call lambda function later
print(add(5, 10))

# 2. Lambda with map() - map() applies function to each iterable elements
numbers = [1, 2, 3, 4]
squared = list(map(lambda number: number ** 2, numbers))
print(squared)

# 3. Lambda with filter() - filter() will return those element which satisfy specified condition
numbers = [1, 2, 4, 6, 8, 0, 7]
even = list(filter(lambda number: number % 2 == 0, numbers))
print(even)

# 4. Lambda with reduce() - reduce() return an single value which we got after applying lambda function to all element
numbers = [1, 2, 3, 4, 5]
all_multiplication = reduce(lambda x, y : x * y, numbers)
print(all_multiplication)