#!/usr/bin/python3
import random

# Generate a random integer between -10 and 10 (inclusive)
number = random.randint(-10, 10)

# Print the random number
print(f"{number} is ", end="")

# Check if the number is positive, zero, or negative and print the result
if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
