# =========================================
# Python Functions
# =========================================

# A function is a reusable block of code
# that performs a specific task.

# Why use functions?
# ✔ Reuse code
# ✔ Make programs easier to read
# ✔ Reduce duplication
# ✔ Easier to maintain


# =========================================
# 1. Creating a Function
# =========================================

def greet():
    print("Hello, Welcome to Python!")

greet()

# Syntax:
#
# def function_name():
#     code


# =========================================
# 2. Function with Parameters
# =========================================

def greet(name):
    print(f"Hello, {name}!")

greet("Sandesh")
greet("John")

# Parameters are variables inside the function.
# Arguments are the actual values passed.


# =========================================
# 3. Function with Multiple Parameters
# =========================================

def introduce(name, age):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")

introduce("Sandesh", 22)


# =========================================
# 4. Returning a Value
# =========================================

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# return sends a value back to the caller.


# =========================================
# 5. Difference Between print() and return
# =========================================

def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

add_print(5, 3)

result = add_return(5, 3)
print(result)

# print() displays a value.
# return gives the value back so it can be reused.


# =========================================
# 6. Default Parameters
# =========================================

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Sandesh")

# If no argument is passed,
# the default value is used.


# =========================================
# 7. Keyword Arguments
# =========================================

def student(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student(age=22, name="Sandesh")

# Order doesn't matter when using keywords.


# =========================================
# 8. Positional Arguments
# =========================================

def multiply(a, b):
    return a * b

print(multiply(5, 10))

# Here:
# 5 -> a
# 10 -> b


# =========================================
# 9. Variable Number of Arguments (*args)
# =========================================

def add_numbers(*numbers):
    total = sum(numbers)
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(5, 10, 15, 20))

# *args collects multiple positional arguments
# into a tuple.


# =========================================
# 10. Variable Keyword Arguments (**kwargs)
# =========================================

def display_info(**person):
    print(person)

display_info(
    name="Sandesh",
    age=22,
    city="Pokhara"
)

# **kwargs collects keyword arguments
# into a dictionary.


# =========================================
# 11. Scope (Local Variable)
# =========================================

def show_name():
    name = "Sandesh"
    print(name)

show_name()

# print(name)
# Error!
# Local variables only exist inside the function.


# =========================================
# 12. Global Variable
# =========================================

name = "Python"

def display():
    print(name)

display()

# Global variables can be accessed
# inside functions.


# =========================================
# 13. Using global Keyword
# =========================================

count = 0

def increment():
    global count
    count += 1

increment()

print(count)

# Use global carefully.
# Returning values is usually a better practice.


# =========================================
# 14. Function Calling Another Function
# =========================================

def greet():
    print("Hello!")

def welcome():
    greet()
    print("Welcome!")

welcome()


# =========================================
# 15. Recursive Function
# =========================================

def countdown(number):

    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)

countdown(5)

# A recursive function calls itself.


# =========================================
# 16. Lambda Functions
# =========================================

square = lambda x: x * x

print(square(5))

# Same as:
#
# def square(x):
#     return x * x

# Lambdas are small anonymous functions.


# =========================================
# 17. Type Hints (Optional)
# =========================================

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))

# Type hints improve readability and
# editor support, but Python does not
# enforce them at runtime.


# =========================================
# 18. Docstrings
# =========================================

def divide(a, b):
    """
    Returns the result of dividing a by b.
    """
    return a / b

print(divide(10, 2))

# Docstrings describe what a function does.


# =========================================
# Real World Example
# =========================================

def calculate_total(price, quantity):
    total = price * quantity
    return total

total = calculate_total(150, 3)

print(f"Total Price: Rs. {total}")


# =========================================
# Quick Summary
# =========================================

# Creating a Function
# -------------------
# def function_name():
#     code


# Returning Values
# ----------------
# return value


# Parameters
# ----------
# def greet(name):


# Default Parameters
# ------------------
# def greet(name="Guest"):


# Keyword Arguments
# -----------------
# greet(name="Sandesh")


# Variable Arguments
# ------------------
# *args    -> Tuple
# **kwargs -> Dictionary


# Scope
# -----
# Local Variables
# Global Variables


# Advanced
# --------
# Lambda Functions
# Recursion
# Type Hints
# Docstrings


# Remember
# --------
# ✔ Functions help eliminate repeated code.
# ✔ Use return when you need the result later.
# ✔ Parameters receive values; arguments are the values you pass.
# ✔ Prefer small, single-purpose functions.
# ✔ In real-world backend development, you'll write functions constantly for
#   handling requests, validating data, querying databases, and processing business logic.