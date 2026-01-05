# Linear Search Algorithm implementation in Python
# Use "python search_algorithms/linear_search.py" in the terminal to run this code

# Linear Search Algorithm No Index
arr = [5, 3, 7, 8, 4]

print("No index linear search")
target_value = int(input("Enter a value to search for: "))

if target_value in arr:
    print("Value found")
else:
    print("Value not found")


# Linear Search Algorithm With Index
arr2 = [7, 2, 9, 1, 6]
found = False
found_index = None

print("With index linear search")
target_value2 = int(input("Enter a value to search for: "))

for index in range(len(arr2)):
    if arr2[index] == target_value2:
        found = True
        found_index = index
        break

if found:
    print("Value found at index", found_index)
if not found:
    print("Value not found")