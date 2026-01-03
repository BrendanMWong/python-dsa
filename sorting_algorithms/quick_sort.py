# Quick Sort Implementation in Python
# Use "python sorting/quick_sort.py" in the terminal to run this code

# Easy to remember implementation of Quick Sort
def quicksort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Recursive case
    pivot = arr[len(arr) // 2]
    left_arr = []
    middle_arr = []
    right_arr = []

    for element in arr:
        if element < pivot: 
            left_arr.append(element) 
        elif element > pivot: 
            right_arr.append(element) 
        else:
            middle_arr.append(element) 

    return quicksort(left_arr) + (middle_arr) + quicksort(right_arr)

arr = [4, 6, 8, 2, 10]
print(quicksort(arr))



# Harder to remember, in-place Quick Sort textbook version
def textbook_quicksort(arr, left_index, right_index):
    # Base case
    if left_index >= right_index:
        return

    # Recursive case
    pivot = arr[(left_index + right_index) // 2]

    # Replaces left_arr and right_arr
    left_pointer = left_index
    right_pointer = right_index

    while left_pointer <= right_pointer:

        # Move left_pointer until element belongs on the right side
        while arr[left_pointer] < pivot:
            left_pointer += 1

        # Move right_pointer until element belongs on the left side
        while arr[right_pointer] > pivot:
            right_pointer -= 1

        # Swap misplaced elements
        if left_pointer <= right_pointer:
            arr[left_pointer], arr[right_pointer] = (
                arr[right_pointer],
                arr[left_pointer]
            )
            left_pointer += 1
            right_pointer -= 1

    textbook_quicksort(arr, left_index, right_pointer)
    textbook_quicksort(arr, left_pointer, right_index)

arr2 = [4, 6, 8, 2, 10]
textbook_quicksort(arr2, 0, len(arr2) - 1)
print(arr2)