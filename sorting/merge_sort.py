# Merge Sort Implementation in Python
# Use "python sorting/merge_sort.py" in the terminal to run this code

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))

def merge(left_arr, right_arr):
    merged_list = []
    left_index_pointer = 0
    right_index_pointer = 0

    while left_index_pointer < len(left_arr) and right_index_pointer < len(right_arr): 
        if left_arr[left_index_pointer] < right_arr[right_index_pointer]:
            merged_list.append(left_arr[left_index_pointer])
            left_index_pointer += 1
        else:
            merged_list.append(right_arr[right_index_pointer])
            right_index_pointer += 1

    merged_list.extend(left_arr[left_index_pointer:]) 
    merged_list.extend(right_arr[right_index_pointer:]) 
    return merged_list

arr = [2, 5, 3, 8, 5, 1, 4, 3]
print(merge_sort(arr))