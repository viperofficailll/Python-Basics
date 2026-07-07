# =========================================
# Python Strings
# =========================================

# A string is a sequence of characters.
# Strings are enclosed in single quotes (' ')
# or double quotes (" ").

name = "Sandesh"
city = 'Pokhara'

print(name)
print(city)


# =========================================
# String Properties
# =========================================

# Strings are:
# ✔ Ordered
# ✔ Immutable (Cannot be changed)
# ✔ Allow duplicate characters

text = "Python"

print(text)

# This will cause an error because strings are immutable.
# text[0] = "J"


# =========================================
# Accessing Characters (Indexing)
# =========================================

language = "Python"

print(language[0])   # P
print(language[1])   # y
print(language[2])   # t
print(language[-1])  # n (Last character)
print(language[-2])  # o (Second last)


# =========================================
# String Slicing
# =========================================

word = "Programming"

print(word[0:4])    # Prog
print(word[4:11])   # ramming
print(word[:6])     # Progra
print(word[3:])     # gramming
print(word[-3:])    # ing

# Syntax:
# string[start:end]
# Start is included.
# End is excluded.


# =========================================
# String Length
# =========================================

name = "Sandesh"

print(len(name))    # 8


# =========================================
# String Concatenation
# =========================================

first_name = "Sandesh"
last_name = "Pokhrel"

full_name = first_name + " " + last_name

print(full_name)


# =========================================
# String Repetition
# =========================================

print("Hi! " * 3)

# Output:
# Hi! Hi! Hi!


# =========================================
# Checking if Text Exists
# =========================================

sentence = "Python is awesome"

print("Python" in sentence)      # True
print("Java" in sentence)        # False

print("Java" not in sentence)    # True


# =========================================
# Common String Methods
# =========================================

text = "python programming"

print(text.upper())          # PYTHON PROGRAMMING
print(text.lower())          # python programming
print(text.title())          # Python Programming
print(text.capitalize())     # Python programming

# Methods do not change the original string.
# They return a new string.


# =========================================
# Removing Extra Spaces
# =========================================

text = "   Hello World   "

print(text.strip())      # Remove spaces from both ends
print(text.lstrip())     # Remove left spaces
print(text.rstrip())     # Remove right spaces


# =========================================
# Replacing Text
# =========================================

text = "I love Java"

new_text = text.replace("Java", "Python")

print(new_text)


# =========================================
# Splitting Strings
# =========================================

languages = "Python,Java,C#,Go"

result = languages.split(",")

print(result)

# Output:
# ['Python', 'Java', 'C#', 'Go']


# =========================================
# Joining Strings
# =========================================

languages = ["Python", "Java", "Go"]

result = " - ".join(languages)

print(result)

# Output:
# Python - Java - Go


# =========================================
# Finding Text
# =========================================

text = "Python Programming"

print(text.find("Program"))   # 7
print(text.find("Java"))      # -1 (Not found)


# =========================================
# Counting Characters
# =========================================

text = "banana"

print(text.count("a"))     # 3
print(text.count("n"))     # 2


# =========================================
# Startswith and Endswith
# =========================================

filename = "resume.pdf"

print(filename.startswith("res"))   # True
print(filename.endswith(".pdf"))    # True


# =========================================
# String Formatting (Recommended)
# =========================================

name = "Sandesh"
age = 22

print(f"My name is {name}.")
print(f"I am {age} years old.")

# f-strings are the recommended way
# to format strings in modern Python.


# =========================================
# Escape Characters
# =========================================

print("Hello\nWorld")      # New line
print("Hello\tWorld")      # Tab
print("He said \"Hi\"")    # Double quote
print("C:\\Users\\Sandesh") # Backslash


# =========================================
# Useful String Checks
# =========================================

text = "Python123"

print(text.isalpha())     # False (Contains numbers)
print(text.isdigit())     # False (Contains letters)
print(text.isalnum())     # True (Letters + Numbers)
print(text.islower())     # False
print(text.isupper())     # False


# =========================================
# Quick Summary
# =========================================

# Creating Strings
# ----------------
# "Hello"
# 'Hello'

# Accessing Characters
# --------------------
# string[0]
# string[-1]

# Slicing
# -------
# string[start:end]

# Useful Functions
# ----------------
# len()
# upper()
# lower()
# title()
# capitalize()
# strip()
# replace()
# split()
# join()
# find()
# count()
# startswith()
# endswith()

# Operators
# ---------
# +    Concatenate strings
# *    Repeat strings
# in   Check if text exists

# Formatting
# ----------
# f"Hello {name}"

# Remember:
# Strings are immutable.
# Methods return a new string instead of modifying the original.