# =========================================
# Python Operators
# =========================================

# Operators are symbols used to perform
# operations on variables and values.

# Main Types:
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Assignment Operators
# 5. Membership Operators
# 6. Identity Operators
# 7. Bitwise Operators (Advanced)


# =========================================
# 1. Arithmetic Operators
# =========================================

a = 10
b = 3

print(a + b)    # Addition -> 13
print(a - b)    # Subtraction -> 7
print(a * b)    # Multiplication -> 30
print(a / b)    # Division -> 3.3333
print(a // b)   # Floor Division -> 3
print(a % b)    # Modulus (Remainder) -> 1
print(a ** b)   # Exponent (Power) -> 1000


# =========================================
# 2. Comparison Operators
# =========================================

x = 10
y = 20

print(x == y)   # Equal -> False
print(x != y)   # Not Equal -> True
print(x > y)    # Greater Than -> False
print(x < y)    # Less Than -> True
print(x >= y)   # Greater Than or Equal -> False
print(x <= y)   # Less Than or Equal -> True

# Comparison operators always return True or False.


# =========================================
# 3. Logical Operators
# =========================================

age = 22
has_license = True

# and -> Both conditions must be True
print(age >= 18 and has_license)

# or -> At least one condition must be True
print(age >= 18 or has_license)

# not -> Reverses the result
print(not has_license)


# =========================================
# 4. Assignment Operators
# =========================================

num = 10

num += 5      # num = num + 5
print(num)

num -= 2      # num = num - 2
print(num)

num *= 3      # num = num * 3
print(num)

num /= 2      # num = num / 2
print(num)

num //= 2     # Floor division assignment
print(num)

num %= 3      # Modulus assignment
print(num)

num **= 2     # Power assignment
print(num)


# =========================================
# 5. Membership Operators
# =========================================

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)        # True
print("Orange" in fruits)       # False

print("Orange" not in fruits)   # True

# Used to check whether a value exists in a collection.


# =========================================
# 6. Identity Operators
# =========================================

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True (same object)
print(a is c)       # False (different objects)

print(a == c)       # True (same values)

print(a is not c)   # True

# == compares values.
# is compares memory location (object identity).


# =========================================
# 7. Bitwise Operators (Advanced)
# =========================================

a = 5      # Binary: 0101
b = 3      # Binary: 0011

print(a & b)    # AND -> 1
print(a | b)    # OR -> 7
print(a ^ b)    # XOR -> 6
print(~a)       # NOT -> -6
print(a << 1)   # Left Shift -> 10
print(a >> 1)   # Right Shift -> 2

# Mostly used in low-level programming,
# networking, embedded systems, and optimization.


# =========================================
# Quick Summary
# =========================================

# Arithmetic
# ----------
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor Division
# %   Modulus (Remainder)
# **  Power

# Comparison
# ----------
# ==
# !=
# >
# <
# >=
# <=

# Logical
# -------
# and
# or
# not

# Assignment
# ----------
# =
# +=
# -=
# *=
# /=
# //=
# %=
# **=

# Membership
# ----------
# in
# not in

# Identity
# --------
# is
# is not

# Bitwise (Advanced)
# ------------------
# &
# |
# ^
# ~
# <<
# >>