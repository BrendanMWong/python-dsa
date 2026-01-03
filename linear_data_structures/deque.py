# Deque implementation in Python
# Use "python linear_data_structures/deque.py" in the terminal to run this code

from collections import deque

arr = [3, 5, 2, 6, 7]
deque_arr = deque(arr)
print(deque_arr)

# Add to right
deque_arr.append(8)
print(deque_arr)

# Add to left
deque_arr.appendleft(1)
print(deque_arr)

# Remove from right
deque_arr.pop()
print(deque_arr)

# Remove from left
deque_arr.popleft()
print(deque_arr)