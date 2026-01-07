# Dictionary implemenation in Python
# Use "python hash_data_structures/dict.py" in the terminal to run this code

# Creating a dictionary
data = {
    "apple": 3,
    "banana": 5,
    "orange": 2
}

# Print the whole dictionary
print(data)

# Accessing values by keys
print(data["apple"])
print(data["orange"])

# Adding and updating key-value pairs
data["grape"] = 7
print(data)

data["banana"] = 10
print(data)

# Checking for key existence
if "apple" in data:
    print("Apple is in the dictionary")

if "pear" not in data:
    print("Pear is not in the dictionary")

# Iterating through keys and values
for key in data:
    print("key: " + str(key) + ", value: " + str(data[key]))

# Alternative way to iterate through keys and values
# .keys() method returns keys
# .values() method returns values
# .items() method returns key-value pairs
for key, value in data.items():
    print("key: " + str(key) + ", value: " + str(data[key]))

# Deleting a key-value pair
del data["orange"]
print(data)