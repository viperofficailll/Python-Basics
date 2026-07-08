"""
================================================================================
                                 DECORATORS
================================================================================

WHAT IS A DECORATOR?
- A decorator is a design pattern that allows you to modify or extend the behavior
  of a function or method WITHOUT permanently changing its original code.
- In Python, functions are "first-class citizens," meaning they can be passed around
  as arguments into other functions, just like numbers or strings.

WHY USE THEM?
- Don't Repeat Yourself (DRY): If you have 20 functions that all need to check if a
  user is logged in, or all need to log how long they take to run, you don't want
  to write that code 20 times. You write one decorator and apply it to all 20.
"""

import time

# ================================================================================
# 1. THE BASICS: HOW A DECORATOR WORKS UNDER THE HOOD
# ================================================================================


def my_decorator(original_function):
    """
    A decorator is just a function that takes another function,
    wraps it with some extra features, and returns the modified wrapper.
    """

    def wrapper():
        print("Something is happening BEFORE the original function runs.")
        original_function()  # Running the actual function
        print("Something is happening AFTER the original function runs.")

    return wrapper


# The Pythonic way to use a decorator is using the '@' symbol right above a function.
@my_decorator
def say_hello():
    print("Hello, World!")


print("--- 1. Basic Decorator Example ---")
say_hello()


# ================================================================================
# 2. HANDLING ARGUMENTS (Using *args and **kwargs)
# ================================================================================
# If your original function takes arguments, your wrapper inside the decorator
# must be able to accept them. We use *args and **kwargs to accept ANY arguments.


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # Call the original function and get its result
        result = func(*args, **kwargs)
        # Modify the result
        return result.upper()

    return wrapper


@uppercase_decorator
def greet(name):
    return f"good morning, {name}"


print("\n--- 2. Decorator with Arguments ---")
print(greet("alice"))


# ================================================================================
# 3. COMMON USE CASE: PERFORMANCE TIMING (A Real-World Example)
# ================================================================================
# A very common use case is tracking how long a function takes to execute.


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)  # Run the actual function

        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f"[LOG] Function '{func.__name__}' took {execution_time:.6f} seconds to run."
        )
        return result

    return wrapper


@timer_decorator
def waste_time():
    # A simple loop to consume time
    total = 0
    for i in range(10_000_000):
        total += i
    return total


print("\n--- 3. Real-World Use Case: Timing ---")
waste_time()


# ================================================================================
# 4. OTHER COMMON REAL-WORLD USE CASES
# ================================================================================
"""
You will see decorators everywhere in professional Python programming:

1. Authentication/Authorization (Web Dev - Flask/Django):
   @login_required
   def view_user_profile():
       ...

2. Rate Limiting (API design):
   @slow_down_requests
   def fetch_data_from_api():
       ...

3. Caching (Performance optimization):
   @lru_cache(maxsize=128)
   def complex_math_calculation(n):
       ...
"""
