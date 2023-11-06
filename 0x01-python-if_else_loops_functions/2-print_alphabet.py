#!/usr/bin/python3

# Intialize and empty string to store the alphabet
alphabet = " "

# Loop through the ASCII lowercase alphabet
for char in range(ord('a'), ord('z') + 1):
    alphabet += chr(char)

# Print the alphabet without a new line
print("{}".format(alphabet), end=" ")
