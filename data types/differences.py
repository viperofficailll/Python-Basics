# ==========================
# Python Data Types Explained
# ==========================

# LIST []
# ------
# - Ordered collection of items
# - Can add, remove, and modify items (Mutable)
# - Allows duplicate values
# - Access items using index

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")      # Add item
fruits[1] = "Grapes"         # Modify item

print(fruits)


# TUPLE ()
# --------
# - Ordered collection of items
# - Cannot be changed after creation (Immutable)
# - Allows duplicate values
# - Access items using index
# - Slightly faster than lists

coordinates = (28.2096, 83.9856)

print(coordinates)

# This will cause an error
# coordinates[0] = 100


# DICTIONARY {}
# -------------
# - Stores data as Key : Value pairs
# - Mutable (can add, remove, and update)
# - Access values using keys instead of indexes
# - Keys must be unique

student = {
    "name": "Sandesh",
    "age": 22,
    "city": "Pokhara"
}

print(student["name"])      # Access value

student["age"] = 23         # Update value
student["college"] = "ABC College"  # Add new key-value pair

print(student)


# ==========================
# Quick Comparison
# ==========================

# List       -> []  -> Mutable  -> Uses Index
# Tuple      -> ()  -> Immutable -> Uses Index
# Dictionary -> {}  -> Mutable  -> Uses Keys

# Examples:
# List       -> Shopping Cart ["Burger", "Pizza"]
# Tuple      -> GPS Coordinates (28.20, 83.98)
# Dictionary -> User Profile {"name": "Sandesh", "age": 22}