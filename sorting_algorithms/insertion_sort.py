# Insertion Sort Implementation in Python
# Use "python sorting/insertion_sort.py" in the terminal to run this code

arr = [3, 5, 4, 1, 2, 8, 7, 6, 10, 9]

for index in range(1, len(arr)): 
    for current_index in range(index, 0, -1):  
        if arr[current_index] < arr[current_index - 1]:  
            arr[current_index], arr[current_index - 1] = arr[current_index - 1], arr[current_index]  
        else:
            break  

print(arr)