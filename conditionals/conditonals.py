# =========================================
# Python Conditionals (if, elif, else)
# =========================================

# Conditionals allow your program to make
# decisions based on True or False conditions.


# =========================================
# 1. Simple if Statement
# =========================================

age = 20

if age >= 18:
    print("You are an adult.")

# The code inside the if block only runs
# if the condition is True.


# =========================================
# 2. if...else Statement
# =========================================

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

# else executes when the if condition is False.


# =========================================
# 3. if...elif...else Statement
# =========================================

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# elif means "else if".
# Python checks each condition from top to bottom.
# As soon as one condition is True, the remaining
# conditions are skipped.


# =========================================
# 4. Multiple Conditions (and)
# =========================================

age = 22
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")


# =========================================
# 5. Multiple Conditions (or)
# =========================================

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today.")
else:
    print("Go to work.")


# =========================================
# 6. Using not
# =========================================

is_logged_in = False

if not is_logged_in:
    print("Please log in.")
else:
    print("Welcome!")


# =========================================
# 7. Nested if Statements
# =========================================

age = 22
has_license = True

if age >= 18:
    print("Adult")

    if has_license:
        print("Can drive")
    else:
        print("Needs a license")

else:
    print("Minor")


# =========================================
# 8. Comparing Strings
# =========================================

language = "Python"

if language == "Python":
    print("Correct language!")
else:
    print("Different language.")


# =========================================
# 9. Membership in Conditionals
# =========================================

fruits = ["Apple", "Banana", "Mango"]

if "Banana" in fruits:
    print("Banana is available.")
else:
    print("Banana is not available.")


# =========================================
# 10. Checking for Empty Values
# =========================================

name = ""

if name:
    print("Name entered.")
else:
    print("Name is empty.")

# Empty strings, empty lists, empty dictionaries,
# and the number 0 evaluate to False.


# =========================================
# 11. Using pass
# =========================================

age = 20

if age >= 18:
    pass

# pass is a placeholder.
# It lets you leave a block empty without causing an error.


# =========================================
# 12. Ternary (One-Line if...else)
# =========================================

age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)

# Syntax:
# value_if_true if condition else value_if_false


# =========================================
# 13. Real World Example
# =========================================

username = "Sandesh"
password = "python123"

if username == "Sandesh" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


# =========================================
# 14. Input with Conditionals
# =========================================

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# =========================================
# Truthy and Falsy Values
# =========================================

# These are considered False:
#
# False
# None
# 0
# 0.0
# ""
# []
# ()
# {}
# set()
#
# Everything else is generally considered True.


# =========================================
# Quick Summary
# =========================================

# if
# --
# if condition:
#     code


# if...else
# ----------
# if condition:
#     code
# else:
#     code


# if...elif...else
# ----------------
# if condition:
#     code
# elif condition:
#     code
# else:
#     code


# Logical Operators
# -----------------
# and
# or
# not


# Comparison Operators
# --------------------
# ==
# !=
# >
# <
# >=
# <=


# Membership Operators
# --------------------
# in
# not in


# Remember:
# ----------
# ✔ Every condition ends with a colon (:)
# ✔ Indentation defines the code block.
# ✔ Conditions evaluate to either True or False.
# ✔ Python executes only the first matching condition in an if...elif...else chain.