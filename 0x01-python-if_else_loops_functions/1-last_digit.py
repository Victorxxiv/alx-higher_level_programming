#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Calculate the last digit
last_digit = abs(number) % 10

# Initialize the message variable
message = "Last digit of {} is {} and is"

# Determine the last digit
if last_digit > 5:
    message += " greater than 5"
elif last_digit == 0:
    message += " 0"
else:
    message += " less than 6 and not 0"

# Print the result
print(message.format(number, last_digit))
