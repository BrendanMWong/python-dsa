# Selection Sort Implementation in Python
# Use "python selection_sort.py" in the terminal to run this code

arr = [2, 5, 3, 1, 4, 8, 7, 6, 10, 9]

for passes in range(len(arr) - 1):
    min_index_value = passes
    for current_index in range(passes + 1, len(arr)):
        if arr[current_index] < arr[min_index_value]:
            min_index_value = current_index
    arr[passes], arr[min_index_value] = arr[min_index_value], arr[passes]

print(arr)
