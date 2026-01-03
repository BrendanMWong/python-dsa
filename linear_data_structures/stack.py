# Stack implementation in Python
# Use "python linear_data_structures/stack.py" in the terminal to run this code

from collections import deque

arr = [3, 5, 2, 6, 7]
stack_arr = deque(arr)
print(stack_arr)

# Add to right
stack_arr.append(8)
print(stack_arr)

# Remove from right
stack_arr.pop()
print(stack_arr)

