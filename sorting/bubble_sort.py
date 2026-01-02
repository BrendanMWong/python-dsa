# Bubble Sort Implementation in Python
# Use "python sorting/bubble_sort.py" in the terminal to run this code

arr = [4, 2, 3, 1, 5, 7, 6, 9, 8, 0, 12, 11, 10, 14, 13]

for index in range(len(arr) - 1):  
    for current_index in range(len(arr) - 1 - index): 
    # "-1" prevents out of bounds error, "- count" shrinks the array 
        if arr[current_index] > arr[current_index + 1]: 
            arr[current_index], arr[current_index + 1] = arr[current_index + 1], arr[current_index]

print(arr)