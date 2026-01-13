# Python DSA

A collection of Python implementations of common data structures and algorithms, organized by category for reference.

## Time Complexity

For this repository:

Access: access by position or arbitrary element unless the structure explicitly defines access.

For stack, queue, and deque access, time complexity is based on valid ends only.

Heap access is explicitly defined as the root, time complexity is not based on accessing an element deeper in the tree.

| Data Structure | Access (Avg) | Access (Worst) | Search (Avg) | Search (Worst) | Insert (Avg) | Insert (Worst) | Delete (Avg) | Delete (Worst) |
|---------------|--------------|----------------|--------------|----------------|--------------|----------------|--------------|----------------|
| Array / List  | O(1)         | O(1)           | O(n)         | O(n)           | O(n)         | O(n)           | O(n)         | O(n)           |
| Linked List   | O(n)         | O(n)           | O(n)         | O(n)           | O(1)         | O(1)           | O(1)         | O(1)           |
| Stack         | O(n)         | O(n)           | O(n)         | O(n)           | O(1)         | O(1)           | O(1)         | O(1)           |
| Queue         | O(n)         | O(n)           | O(n)         | O(n)           | O(1)         | O(1)           | O(1)         | O(1)           |
| Deque         | O(n)         | O(n)           | O(n)         | O(n)           | O(1)         | O(1)           | O(1)         | O(1)           |
| String        | O(1)         | O(1)           | O(n)         | O(n)           | O(n)         | O(n)           | O(n)         | O(n)           |
| Hash Table (Dict) | O(1)     | O(n)           | O(1)         | O(n)           | O(1)         | O(n)           | O(1)         | O(n)           |
| Hash Set      | O(1)         | O(n)           | O(1)         | O(n)           | O(1)         | O(n)           | O(1)         | O(n)           |
| Binary Tree   | O(n)         | O(n)           | O(n)         | O(n)           | O(n)         | O(n)           | O(n)         | O(n)           |
| Binary Search Tree | O(n)    | O(n)           | O(log n)     | O(n)           | O(log n)     | O(n)           | O(log n)     | O(n)           |
| AVL Tree      | O(log n)     | O(log n)       | O(log n)     | O(log n)       | O(log n)     | O(log n)       | O(log n)     | O(log n)       |
| Red-Black Tree| O(log n)     | O(log n)       | O(log n)     | O(log n)       | O(log n)     | O(log n)       | O(log n)     | O(log n)       |
| Heap          | O(1)         | O(1)           | O(n)         | O(n)           | O(log n)     | O(log n)       | O(log n)     | O(log n)       |
| Trie          | O(L)         | O(L)           | O(L)         | O(L)           | O(L)         | O(L)           | O(L)         | O(L)           |
| Graph         | O(1)         | O(1)           | O(V + E)     | O(V + E)       | O(1)         | O(1)           | O(V + E)     | O(V + E)       |

| Algorithm           | Best Case | Average Case | Worst Case | Space Complexity |
|--------------------|-----------|--------------|------------|----------------|
| Linear Search       | O(1)      | O(n)         | O(n)       | O(1)           |
| Binary Search       | O(1)      | O(log n)     | O(log n)   | O(1)           |
| Bubble Sort         | O(n)      | O(n²)        | O(n²)      | O(1)           |
| Selection Sort      | O(n²)     | O(n²)        | O(n²)      | O(1)           |
| Insertion Sort      | O(n)      | O(n²)        | O(n²)      | O(1)           |
| Merge Sort          | O(n log n)| O(n log n)   | O(n log n) | O(n)           |
| Quick Sort          | O(n log n)| O(n log n)   | O(n²)      | O(log n)       |


