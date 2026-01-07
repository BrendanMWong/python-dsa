# Set Implementation in Python
# Use "python hash_data_structures/set.py" in the terminal to run this code

# Creating a set
data = {1, 2, 3, 4, 5}

# Print the whole set
print(data)

# Adding elements
data.add(6)
print(data)

# Removing elements
data.remove(3)
print(data)

# Checking for element existence
print(4 in data)
print(10 in data)

# Iterating through elements
for element in data:
    print(element)

data2 = {4, 5, 6, 7, 8}

# Set operations
union_set = data.union(data2)
intersection_set = data.intersection(data2)

print("Union:", union_set)
print("Intersection:", intersection_set)

diff_set = data.difference(data2)
print("Difference:", diff_set)
