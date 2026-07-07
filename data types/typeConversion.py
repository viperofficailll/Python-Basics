# =========================================
# Implicit and Explicit Type Conversion
# =========================================

# Type Conversion
# ----------------
# Type conversion means changing one data type into another.
#
# There are two types:
# 1. Implicit Type Conversion (Done automatically by Python)
# 2. Explicit Type Conversion (Done manually by the programmer)


# =========================================
# 1. Implicit Type Conversion
# =========================================

# Python automatically converts the smaller data type
# into a larger compatible data type.

num1 = 10          # int
num2 = 5.5         # float

result = num1 + num2

print(result)          # 15.5
print(type(result))    # <class 'float'>

# Explanation:
# int + float = float
# Python converts 10 -> 10.0 automatically.


# Another Example

a = True           # bool (True = 1)
b = 5

result = a + b

print(result)          # 6
print(type(result))    # <class 'int'>

# Explanation:
# True becomes 1 automatically.
# 1 + 5 = 6


# =========================================
# 2. Explicit Type Conversion
# =========================================

# The programmer manually converts one data type
# into another using built-in functions.

age = "22"         # String

print(type(age))   # <class 'str'>

age = int(age)     # Convert string to integer

print(age)
print(type(age))   # <class 'int'>


# Convert int to float

num = 50

num = float(num)

print(num)         # 50.0
print(type(num))   # <class 'float'>


# Convert float to int

price = 99.99

price = int(price)

print(price)       # 99
print(type(price)) # <class 'int'>

# Note:
# int() removes the decimal part.
# It does NOT round the number.


# Convert int to string

marks = 95

marks = str(marks)

print(marks)
print(type(marks))     # <class 'str'>


# =========================================
# Common Conversion Functions
# =========================================

# int()    -> Converts to Integer
# float()  -> Converts to Float
# str()    -> Converts to String
# bool()   -> Converts to Boolean
# list()   -> Converts to List
# tuple()  -> Converts to Tuple
# dict()   -> Converts to Dictionary (if valid)


# =========================================
# Example with User Input
# =========================================

# input() always returns a string.

age = input("Enter your age: ")

print(type(age))        # <class 'str'>

age = int(age)          # Explicit conversion

print(type(age))        # <class 'int'>

print("Next year you will be", age + 1)


# =========================================
# Quick Summary
# =========================================

# Implicit Conversion
# -------------------
# ✔ Done automatically by Python
# ✔ No function needed
#
# Example:
# int + float -> float


# Explicit Conversion
# -------------------
# ✔ Done manually by the programmer
# ✔ Uses functions like int(), float(), str()
#
# Example:
# "25" -> int("25") -> 25