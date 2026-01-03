# Queue implementation in Python
# Use "python linear_data_structures/queue.py" in the terminal to run this code

from collections import deque

arr = [3, 5, 2, 6, 7]
queue_arr = deque(arr)
print(queue_arr)

# Add to right
queue_arr.append(8)
print(queue_arr)

# Remove from left
queue_arr.popleft()
print(queue_arr)