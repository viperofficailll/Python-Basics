"""
================================================================================
                           ITERATORS & GENERATORS
================================================================================

WHAT ARE THEY?
- An ITERABLE is anything you can loop over (like a list, tuple, or string).
- An ITERATOR is the actual agent that fetches items one by one behind the scenes.
- A GENERATOR is a special function that simplifies making iterators using the 'yield' keyword.

WHY USE THEM?
Memory Efficiency! If you have 1 million numbers:
- A normal list stores ALL 1 million numbers in RAM at the same time.
- An iterator/generator calculates the next number ONLY when you ask for it.
  It takes almost ZERO memory, no matter how big the data is.
"""

import sys

# ================================================================================
# 1. UNDER THE HOOD: ITERATORS
# ================================================================================
# Any object that implements two magic methods: __iter__() and __next__()


class Counter:
    """A simple custom iterator that counts from 'low' to 'high'"""

    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self  # An iterator must return itself

    def __next__(self):
        if self.current <= self.high:
            result = self.current
            self.current += 1
            return result
        else:
            # When we run out of items, we must raise StopIteration
            raise StopIteration


print("--- 1. Custom Iterator ---")
my_counter = Counter(1, 3)
for num in my_counter:
    print(num)


# ================================================================================
# 2. THE EASY WAY: GENERATORS
# ================================================================================
# Writing custom iterator classes is tedious.
# Generators do the exact same thing but use a function with 'yield'.
# When a function hits 'yield', it pauses and passes the value back.
# When called again, it resumes exactly where it left off!


def counter_generator(low, high):
    """Same as the Counter class above, but way shorter."""
    current = low
    while current <= high:
        yield current
        current += 1


print("\n--- 2. Generator Function ---")
gen = counter_generator(1, 3)
for num in gen:
    print(num)


# ================================================================================
# 3. COMMON USE CASE: PROCESSING MASSIVE DATA (The Memory Saver)
# ================================================================================

# Scenario: Imagine generating 10 million numbers to process.


def list_way():
    # This creates the entire list of 10 million integers in memory at once!
    return [i for i in range(10_000_000)]


def generator_way():
    # This yields one number at a time as requested.
    for i in range(10_000_000):
        yield i


print("\n--- 3. Memory Use Case ---")

huge_list = list_way()
print(f"Size of List in RAM: {sys.getsizeof(huge_list):,} bytes")

huge_gen = generator_way()
print(f"Size of Generator in RAM: {sys.getsizeof(huge_gen):,} bytes")

# Notice how tiny the generator is compared to the list!


# ================================================================================
# 4. COMMON USE CASE: INFINITE STREAMS
# ================================================================================
# You can't store an infinite list in Python because your computer would crash.
# But you CAN have an infinite generator because it only computes the current value.


def infinite_even_numbers():
    num = 0
    while True:
        yield num
        num += 2


print("\n--- 4. Infinite Stream Example ---")
evens = infinite_even_numbers()

# We can safely pull out as many as we want using the next() function
print(next(evens))  # 0
print(next(evens))  # 2
print(next(evens))  # 4
print(next(evens))  # 6
# The loop won't run forever because we control when we call next()!
