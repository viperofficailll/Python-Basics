# =========================================
# Python Class Variables
# =========================================

# A class variable belongs to the class itself.
# It is shared by ALL objects (instances) of that class.

# If one object changes a class variable,
# the change is reflected in all other objects
# (unless an instance variable with the same name is created).


# =========================================
# 1. Creating a Class Variable
# =========================================

class Employee:

    company = "Google"   # Class Variable

    def __init__(self, name, salary):
        self.name = name         # Instance Variable
        self.salary = salary     # Instance Variable


emp1 = Employee("Sandesh", 50000)
emp2 = Employee("John", 60000)

print(emp1.company)
print(emp2.company)

# Output:
# Google
# Google


# =========================================
# 2. Instance Variables
# =========================================

# Instance variables belong to each object.
# Every object has its own copy.

print(emp1.name)
print(emp2.name)

# Output:
# Sandesh
# John


# =========================================
# 3. Changing a Class Variable
# =========================================

Employee.company = "Microsoft"

print(emp1.company)
print(emp2.company)

# Output:
# Microsoft
# Microsoft

# Since company is a class variable,
# changing it affects every object.


# =========================================
# 4. Creating an Instance Variable with
#    the Same Name
# =========================================

emp1.company = "Amazon"

print(emp1.company)
print(emp2.company)
print(Employee.company)

# Output:
# Amazon
# Microsoft
# Microsoft

# Explanation:
# emp1 now has its own company variable.
# emp2 still uses the class variable.


# =========================================
# 5. Accessing Class Variables
# =========================================

print(Employee.company)

print(emp2.company)

# Best Practice:
# Access class variables using the class name.

# Employee.company


# =========================================
# 6. Using Class Variables as Counters
# =========================================

class Student:

    total_students = 0

    def __init__(self, name):
        self.name = name

        Student.total_students += 1


s1 = Student("Sandesh")
s2 = Student("John")
s3 = Student("Alice")

print(Student.total_students)

# Output:
# 3


# =========================================
# 7. Another Practical Example
# =========================================

class Employee:

    raise_percentage = 1.10

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_percentage)


emp = Employee("Sandesh", 50000)

emp.apply_raise()

print(emp.salary)

# Output:
# 55000

# Changing the raise percentage

Employee.raise_percentage = 1.20

emp2 = Employee("John", 50000)

emp2.apply_raise()

print(emp2.salary)

# Output:
# 60000


# =========================================
# 8. Class Variable vs Instance Variable
# =========================================

class Dog:

    species = "Canine"      # Class Variable

    def __init__(self, name):
        self.name = name    # Instance Variable


dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)
print(dog2.species)

print(dog1.name)
print(dog2.name)

# species is shared.
# name is unique.


# =========================================
# Common Use Cases
# =========================================

# ✔ Company Name
# ✔ Tax Rate
# ✔ Discount Percentage
# ✔ Employee Count
# ✔ Student Count
# ✔ Configuration Values
# ✔ Application Version


# =========================================
# Quick Summary
# =========================================

# Class Variable
# --------------
# - Declared inside the class
# - Outside __init__()
# - Shared by every object
# - Access using ClassName.variable

# Example:
#
# class Employee:
#     company = "Google"


# Instance Variable
# -----------------
# - Declared inside __init__()
# - Uses self
# - Each object has its own copy

# Example:
#
# self.name = name
# self.salary = salary


# Accessing Variables
# -------------------
# Employee.company
# emp.company
# emp.name


# Remember:
# ----------
# ✔ Class variables belong to the class.
# ✔ Instance variables belong to objects.
# ✔ Changing a class variable affects every object
#   unless an instance variable with the same name exists.
# ✔ Use class variables for data shared by all objects.