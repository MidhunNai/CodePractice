# Exception Handling in Python

"""
Exception handling is a powerful feature in Python that allows you to manage and respond to unexpected errors that may occur during code execution. Without it, your program might crash abruptly.

Syntax
try:
    # Code that may raise an exceptionYa
expect ExceptionType:
    # Code that runs if the exception occurs
"""
# try:
#     num = int(input("Enter any number : "))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# Handling multiple exception
# try:
#     num = int(input("Enter any number : "))
#     result = 10 / num
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# except IndexError:
#     print("List index is out of range")
# except ValueError:
#     print("Invalid input. Please enter a valid number")

# else and finally - else runs when there is no errors and finally runs every time
# try:
#     num = int(input("Enter any number : "))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# else:
#     print("No error occurred.")
# finally:
#     print("Program ended.")

# raise - we can manually trigger exception using raise keyword
def check_age(age):
    if age < 18:
        raise ValueError("Error: Age must be 18 or above.")
    print("Age verified.")
try:
    check_age(15)
except ValueError as e:
    print(e)

# Catching any exception - use except Exception:
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except Exception as e:
    print(f"Error: {e}")