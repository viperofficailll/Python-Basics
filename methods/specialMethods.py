# ============================================================
# File: special_methods.py
# Topic: Python Special Methods (Dunder Methods) & __main__
# ============================================================
#
# This file explains:
# 1. __init__
# 2. self
# 3. __str__
# 4. __repr__
# 5. __len__
# 6. __getitem__
# 7. __setitem__
# 8. __contains__
# 9. __iter__
# 10. __next__
# 11. __call__
# 12. __add__
# 13. __sub__
# 14. __mul__
# 15. __truediv__
# 16. __eq__
# 17. __lt__
# 18. __gt__
# 19. __enter__ & __exit__
# 20. if __name__ == "__main__"
#
# These methods are called "Special Methods"
# or "Dunder Methods" (Double UNDERSCORE Methods).
#
# Python automatically calls these methods in
# different situations.
#
# Example:
#
# print(obj)  ---> obj.__str__()
# len(obj)    ---> obj.__len__()
# obj1 + obj2 ---> obj1.__add__(obj2)
#
# ============================================================


print("\n==============================")
print("1. __init__()")
print("==============================")

# __init__ is called automatically when an object is created.
# It is known as the constructor.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Sandesh", 22)

print(student.name)
print(student.age)


# ------------------------------------------------------------


print("\n==============================")
print("2. self")
print("==============================")

# self refers to the CURRENT object.
# Every object has its own copy of instance variables.

class Car:

    def __init__(self, brand):
        self.brand = brand


car1 = Car("Tesla")
car2 = Car("BMW")

print(car1.brand)
print(car2.brand)


# ------------------------------------------------------------


print("\n==============================")
print("3. __str__()")
print("==============================")

# Controls what print(object) displays.

class Book:

    def __str__(self):
        return "Python Book"


book = Book()

print(book)

# Without __str__:
#
# <__main__.Book object at 0x...>


# ------------------------------------------------------------


print("\n==============================")
print("4. __repr__()")
print("==============================")

# Used mainly for debugging.

class Laptop:

    def __repr__(self):
        return "Laptop()"


laptop = Laptop()

print(laptop)


# ------------------------------------------------------------


print("\n==============================")
print("5. __len__()")
print("==============================")

# Makes len(object) work.

class Playlist:

    def __len__(self):
        return 15


playlist = Playlist()

print(len(playlist))


# ------------------------------------------------------------


print("\n==============================")
print("6. __getitem__()")
print("==============================")

# Makes indexing possible.

class Letters:

    def __getitem__(self, index):
        letters = ["A", "B", "C", "D"]
        return letters[index]


letters = Letters()

print(letters[0])
print(letters[2])


# ------------------------------------------------------------


print("\n==============================")
print("7. __setitem__()")
print("==============================")

# Makes assignment using [] possible.

class Scores:

    def __init__(self):
        self.data = [10, 20, 30]

    def __setitem__(self, index, value):
        self.data[index] = value


scores = Scores()

scores[1] = 100

print(scores.data)


# ------------------------------------------------------------


print("\n==============================")
print("8. __contains__()")
print("==============================")

# Makes "in" keyword work.

class Fruits:

    def __contains__(self, item):
        fruits = ["apple", "banana", "orange"]
        return item in fruits


fruits = Fruits()

print("banana" in fruits)
print("grape" in fruits)


# ------------------------------------------------------------


print("\n==============================")
print("9. __iter__()")
print("==============================")

# Allows looping with for.

class Numbers:

    def __iter__(self):
        return iter([1, 2, 3, 4])


numbers = Numbers()

for num in numbers:
    print(num)


# ------------------------------------------------------------


print("\n==============================")
print("10. __next__()")
print("==============================")

# Used together with __iter__.
# Controls what next() returns.

class Counter:

    def __init__(self):
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.count <= 3:
            value = self.count
            self.count += 1
            return value

        raise StopIteration


counter = Counter()

for value in counter:
    print(value)


# ------------------------------------------------------------


print("\n==============================")
print("11. __call__()")
print("==============================")

# Makes an object behave like a function.

class Hello:

    def __call__(self):
        print("Hello World!")


hello = Hello()

hello()


# ------------------------------------------------------------


print("\n==============================")
print("12. __add__()")
print("==============================")

# Defines +

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


a = Number(5)
b = Number(7)

print(a + b)


# ------------------------------------------------------------


print("\n==============================")
print("13. __sub__()")
print("==============================")

# Defines -

class Number2:

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


a = Number2(10)
b = Number2(4)

print(a - b)


# ------------------------------------------------------------


print("\n==============================")
print("14. __mul__()")
print("==============================")

# Defines *

class Number3:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value


a = Number3(5)
b = Number3(6)

print(a * b)


# ------------------------------------------------------------


print("\n==============================")
print("15. __truediv__()")
print("==============================")

# Defines /

class Number4:

    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return self.value / other.value


a = Number4(20)
b = Number4(5)

print(a / b)


# ------------------------------------------------------------


print("\n==============================")
print("16. __eq__()")
print("==============================")

# Defines ==

class User:

    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id


u1 = User(1)
u2 = User(1)

print(u1 == u2)


# ------------------------------------------------------------


print("\n==============================")
print("17. __lt__()")
print("==============================")

# Defines <

class Product:

    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


p1 = Product(100)
p2 = Product(150)

print(p1 < p2)


# ------------------------------------------------------------


print("\n==============================")
print("18. __gt__()")
print("==============================")

# Defines >

class Product2:

    def __init__(self, price):
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product2(500)
p2 = Product2(300)

print(p1 > p2)


# ------------------------------------------------------------


print("\n==============================")
print("19. __enter__() and __exit__()")
print("==============================")

# Used by the "with" statement.

class DemoContext:

    def __enter__(self):
        print("Entering block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving block")


with DemoContext():
    print("Inside with block")


# ------------------------------------------------------------


print("\n==============================")
print("20. if __name__ == '__main__'")
print("==============================")

# Every Python file has a built-in variable called __name__.
#
# If you RUN this file directly:
#
# python special_methods.py
#
# __name__ becomes "__main__"
#
# If another file imports this file:
#
# import special_methods
#
# then __name__ becomes "special_methods"
#
# This lets us run testing code only when the file
# is executed directly.

def greet():
    print("Hello from greet()")


if __name__ == "__main__":
    print("This file is being run directly.")
    greet()


# ============================================================
# QUICK CHEAT SHEET
# ============================================================
#
# __init__       -> Runs when object is created
#
# __str__        -> print(object)
#
# __repr__       -> Debug representation
#
# __len__        -> len(object)
#
# __getitem__    -> object[index]
#
# __setitem__    -> object[index] = value
#
# __contains__   -> value in object
#
# __iter__       -> for loop starts
#
# __next__       -> next() during iteration
#
# __call__       -> object()
#
# __add__        -> +
#
# __sub__        -> -
#
# __mul__        -> *
#
# __truediv__    -> /
#
# __eq__         -> ==
#
# __lt__         -> <
#
# __gt__         -> >
#
# __enter__      -> Start of with block
#
# __exit__       -> End of with block
#
# if __name__ == "__main__":
#               -> Run code only when this file
#                  is executed directly.
#
# ============================================================