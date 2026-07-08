# =========================================
# Python File Handling
# =========================================

"""
File Handling
-------------

File handling allows a program to create,
read, write, update, and delete files.

Examples:
✔ Saving user information
✔ Reading configuration files
✔ Loading AI datasets
✔ Writing logs
✔ Storing reports

Python uses the built-in open() function
to work with files.
"""


# =========================================
# 1. Opening a File
# =========================================

"""
Syntax

open(filename, mode)

filename
---------
The file you want to open.

mode
----
How you want to use the file.
"""

# Example

# file = open("notes.txt", "r")

# Always close the file after using it.

# file.close()


# =========================================
# 2. File Modes
# =========================================

"""
r  -> Read (Default)

w  -> Write
      Creates file if it doesn't exist.
      Overwrites existing file.

a  -> Append
      Adds data to the end of the file.

x  -> Create
      Creates a new file.
      Error if file already exists.

rb -> Read Binary

wb -> Write Binary

r+ -> Read and Write

w+ -> Write and Read
"""


# =========================================
# 3. Reading an Entire File
# =========================================

"""
Suppose notes.txt contains:

Python
Java
C#
"""

# with open("notes.txt", "r") as file:
#     data = file.read()
#     print(data)

"""
Output

Python
Java
C#
"""


# =========================================
# 4. Reading One Line
# =========================================

# with open("notes.txt", "r") as file:
#
#     print(file.readline())
#     print(file.readline())

"""
Output

Python
Java
"""


# =========================================
# 5. Reading All Lines
# =========================================

# with open("notes.txt", "r") as file:
#
#     lines = file.readlines()
#
#     print(lines)

"""
Output

['Python\n', 'Java\n', 'C#']
"""


# =========================================
# 6. Loop Through a File
# =========================================

# with open("notes.txt", "r") as file:
#
#     for line in file:
#
#         print(line.strip())

"""
strip()

Removes extra whitespace
including newlines.
"""


# =========================================
# 7. Writing to a File
# =========================================

"""
w mode

Creates the file if it doesn't exist.

Overwrites everything if it does exist.
"""

# with open("output.txt", "w") as file:
#
#     file.write("Hello World")


# =========================================
# 8. Writing Multiple Lines
# =========================================

# with open("languages.txt", "w") as file:
#
#     file.write("Python\n")
#     file.write("Java\n")
#     file.write("C#\n")


# =========================================
# 9. Appending to a File
# =========================================

"""
Append does NOT erase previous data.
"""

# with open("log.txt", "a") as file:
#
#     file.write("User Logged In\n")


# =========================================
# 10. Using with (Best Practice)
# =========================================

"""
Always prefer

with open()

Why?

Python automatically closes
the file.

No need to call close().
"""

# with open("notes.txt", "r") as file:
#
#     print(file.read())


# =========================================
# 11. Checking if a File Exists
# =========================================

from pathlib import Path

path = Path("notes.txt")

print(path.exists())

"""
Output

True

or

False
"""


# =========================================
# 12. Creating a File
# =========================================

# with open("new_file.txt", "x") as file:
#
#     file.write("First Line")


"""
If the file already exists,

Python raises

FileExistsError
"""


# =========================================
# 13. Deleting a File
# =========================================

import os

# os.remove("new_file.txt")

"""
Always check if the file exists
before deleting it.
"""

# if os.path.exists("new_file.txt"):
#     os.remove("new_file.txt")


# =========================================
# 14. Working with CSV Files
# =========================================

"""
CSV

Comma Separated Values

Example

name,age

Sandesh,22

John,30
"""

import csv

# Writing CSV

# with open("students.csv", "w", newline="") as file:
#
#     writer = csv.writer(file)
#
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Sandesh", 22])
#     writer.writerow(["John", 30])


# Reading CSV

# with open("students.csv", "r") as file:
#
#     reader = csv.reader(file)
#
#     for row in reader:
#
#         print(row)


# =========================================
# 15. Working with JSON
# =========================================

"""
JSON

Most common data format
used in APIs.
"""

import json

student = {
    "name": "Sandesh",
    "age": 22,
    "city": "Pokhara"
}


# Writing JSON

# with open("student.json", "w") as file:
#
#     json.dump(student, file, indent=4)


# Reading JSON

# with open("student.json", "r") as file:
#
#     data = json.load(file)
#
#     print(data)


# =========================================
# 16. Binary Files
# =========================================

"""
Used for

Images

Videos

PDFs

Executables
"""

# with open("image.png", "rb") as file:
#
#     data = file.read()


# =========================================
# 17. Copying a File
# =========================================

# with open("notes.txt", "r") as source:
#
#     content = source.read()
#
# with open("copy.txt", "w") as destination:
#
#     destination.write(content)


# =========================================
# 18. Real World Example
# =========================================

"""
Save user feedback.
"""

feedback = "Great application!\n"

# with open("feedback.txt", "a") as file:
#
#     file.write(feedback)


# =========================================
# 19. Real World Example
# =========================================

"""
Store application logs.
"""

from datetime import datetime

current_time = datetime.now()

log = f"{current_time} : User Logged In\n"

# with open("app.log", "a") as file:
#
#     file.write(log)


# =========================================
# 20. Common Exceptions
# =========================================

"""
FileNotFoundError

PermissionError

FileExistsError
"""

# try:
#
#     with open("abc.txt") as file:
#
#         print(file.read())
#
# except FileNotFoundError:
#
#     print("File not found.")


# =========================================
# Common Mistakes
# =========================================

"""
❌ Forgetting to close files.

Use

with open()

instead.


❌ Using "w"

when you wanted "a"

w

Deletes old contents.


❌ Forgetting newline=""

when writing CSV.


❌ Opening binary files
without rb or wb.


❌ Reading a file
that doesn't exist.
"""


# =========================================
# Interview Questions
# =========================================

"""
Q.

Difference between

read()

readline()

readlines()


read()

Entire file


readline()

One line


readlines()

Returns a list of lines


----------------------------------


Q.

Difference between

w

and

a


w

Overwrite

a

Append


----------------------------------


Q.

Why use

with open()?


Automatically closes the file.


----------------------------------


Q.

Most common file formats?

TXT

CSV

JSON

XML

PDF

Images
"""


# =========================================
# Quick Summary
# =========================================

"""
Opening Files

open(filename, mode)


Best Practice

with open(...)


Modes

r

Read

w

Write

a

Append

x

Create

rb

Read Binary

wb

Write Binary


Useful Methods

read()

readline()

readlines()

write()


Modules

os

pathlib

csv

json


Remember

✔ Always use with open()

✔ Close files automatically

✔ Use JSON for APIs

✔ Use CSV for tabular data

✔ Handle exceptions
"""