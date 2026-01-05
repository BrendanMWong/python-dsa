# Binary Search Algorithm implementation in Python
# Use "python search_algorithms/binary_search.py" in the terminal to run this code

# Sorted list
arr = [1, 3, 5, 7, 9, 11, 13]

target_value = int(input("Enter a value to search for: "))

# Initialize pointers
left = 0
right = len(arr) - 1
found_index = None

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target_value:
        found_index = mid
        break
    elif arr[mid] < target_value:
        left = mid + 1
    else:
        right = mid - 1

if found_index is not None:
    print("Value found at index", found_index)
else:
    print("Value not found")
