# String implementation in Python
# Use "python linear_data_structures/string.py" in the terminal to run this code

s = "datastructures"

# Print the entire string
print(s)

# Access individual characters
print(s[0])
print(s[-1])

# String length
print(len(s))

# Iterate through the string
for char in s:
    print(char)

# Slicing the string
print(s[0:4])
print(s[4:])

# Checking for substrings
print('a' in s)
print('z' in s)

# Strings are immutable, so we create a new string to modify
s = 'D' + s[1:]
print(s)