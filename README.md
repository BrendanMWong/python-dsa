# Python DSA

A collection of Python implementations of common data structures and algorithms, organized by category for reference.

## Time Complexity

For these tables, operations are based on the intended use of the data structure. Access is N/A for data structures that don't support indexing. 

| Data Structure     | Access (Avg) | Access (Worst) | Search (Avg) | Search (Worst) | Insert (Avg) | Insert (Worst) | Delete (Avg) | Delete (Worst) |
| ------------------ | ------------ | -------------- | ------------ | -------------- | ------------ | -------------- | ------------ | -------------- |
| Array / List       | O(1)         | O(1)           | O(n)         | O(n)           | O(n)         | O(n)           | O(n)         | O(n)           |
| Linked List        | N/A          | N/A            | O(n)         | O(n)           | O(1)         | O(1)           | O(1)         | O(1)           |
| Stack              | N/A          | N/A            | O(n)         | O(n)           | O(1)         | O(1)           | O(1)         | O(1)           |
| Queue              | N/A          | N/A            | O(n)         | O(n)           | O(1)         | O(1)           | O(1)         | O(1)           |
| Deque              | N/A          | N/A            | O(n)         | O(n)           | O(1)         | O(1)           | O(1)         | O(1)           |
| String             | O(1)         | O(1)           | O(n)         | O(n)           | O(n)         | O(n)           | O(n)         | O(n)           |
| Hash Table (Dict)  | O(1)         | O(n)           | O(1)         | O(n)           | O(1)         | O(n)           | O(1)         | O(n)           |
| Hash Set           | O(1)         | O(n)           | O(1)         | O(n)           | O(1)         | O(n)           | O(1)         | O(n)           |
| Binary Tree        | N/A          | N/A            | O(n)         | O(n)           | O(n)         | O(n)           | O(n)         | O(n)           |
| Binary Search Tree | N/A          | N/A            | O(log n)     | O(n)           | O(log n)     | O(n)           | O(log n)     | O(n)           |
| AVL Tree           | N/A          | N/A            | O(log n)     | O(log n)       | O(log n)     | O(log n)       | O(log n)     | O(log n)       |
| Red-Black Tree     | N/A          | N/A            | O(log n)     | O(log n)       | O(log n)     | O(log n)       | O(log n)     | O(log n)       |
| Heap               | O(1)         | O(1)           | O(n)         | O(n)           | O(log n)     | O(log n)       | O(log n)     | O(log n)       |
| Trie               | N/A          | N/A            | O(L)         | O(L)           | O(L)         | O(L)           | O(L)         | O(L)           |
| Graph              | N/A          | N/A            | O(V + E)     | O(V + E)       | O(1)         | O(1)           | O(V + E)     | O(V + E)       |

| Algorithm           | Best Case | Average Case | Worst Case | Space Complexity |
|--------------------|-----------|--------------|------------|----------------|
| Linear Search       | O(1)      | O(n)         | O(n)       | O(1)           |
| Binary Search       | O(1)      | O(log n)     | O(log n)   | O(1)           |
| Bubble Sort         | O(n)      | O(n²)        | O(n²)      | O(1)           |
| Selection Sort      | O(n²)     | O(n²)        | O(n²)      | O(1)           |
| Insertion Sort      | O(n)      | O(n²)        | O(n²)      | O(1)           |
| Merge Sort          | O(n log n)| O(n log n)   | O(n log n) | O(n)           |
| Quick Sort          | O(n log n)| O(n log n)   | O(n²)      | O(log n)       |

## Data Structure Time Complexity Explanations

### Array / List
- **Access (Avg/Worst) O(1):** Indexing jumps directly to the memory address.
- **Search (Avg/Worst) O(n):** Elements must be checked sequentially.
- **Insert (Avg/Worst) O(n):** Elements may need to be shifted.
- **Delete (Avg/Worst) O(n):** Removing an element shifts following items.

---

### Linked List
- **Search (Avg/Worst) O(n):** Nodes must be traversed one by one.
- **Insert (Avg/Worst) O(1):** Pointer updates take constant time.
- **Delete (Avg/Worst) O(1):** Node removal only changes links.

---

### Stack
- **Search (Avg/Worst) O(n):** Elements must be popped to inspect.
- **Insert (Avg/Worst) O(1):** Push adds to the top.
- **Delete (Avg/Worst) O(1):** Pop removes the top element.

---

### Queue
- **Search (Avg/Worst) O(n):** Elements must be dequeued to inspect.
- **Insert (Avg/Worst) O(1):** Enqueue adds to the rear.
- **Delete (Avg/Worst) O(1):** Dequeue removes from the front.

---

### Deque
- **Search (Avg/Worst) O(n):** Elements must be traversed.
- **Insert (Avg/Worst) O(1):** Items can be added at either end.
- **Delete (Avg/Worst) O(1):** Items can be removed at either end.

---

### String
- **Access (Avg/Worst) O(1):** Characters are indexable.
- **Search (Avg/Worst) O(n):** Characters must be scanned.
- **Insert (Avg/Worst) O(n):** A new string must be created.
- **Delete (Avg/Worst) O(n):** Characters are copied or shifted.

---

### Hash Table (Dictionary)
- **Access (Avg) O(1):** Hashing locates the bucket quickly.
- **Access (Worst) O(n):** All keys collide into one bucket.
- **Search (Avg) O(1):** Hash lookup is constant time.
- **Search (Worst) O(n):** Collision chains must be scanned.
- **Insert (Avg) O(1):** Key is placed using its hash.
- **Insert (Worst) O(n):** Rehashing or collisions degrade performance.
- **Delete (Avg) O(1):** Key is found via hashing.
- **Delete (Worst) O(n):** Collision chains must be searched.

---

### Hash Set
- **Access (Avg) O(1):** Hashing locates the element.
- **Access (Worst) O(n):** All elements collide.
- **Search (Avg) O(1):** Hash lookup is constant.
- **Search (Worst) O(n):** Collisions force linear scan.
- **Insert (Avg) O(1):** Element is hashed and placed.
- **Insert (Worst) O(n):** Rehashing or collisions occur.
- **Delete (Avg) O(1):** Element is hash-located.
- **Delete (Worst) O(n):** Collision resolution is required.

---

### Binary Tree (Unordered)
- **Search (Avg/Worst) O(n):** Tree may require full traversal.
- **Insert (Avg/Worst) O(n):** Finding a position takes traversal.
- **Delete (Avg/Worst) O(n):** Node must be located first.

---

### Binary Search Tree (Unbalanced)
- **Search (Avg) O(log n):** Tree height is logarithmic on average.
- **Search (Worst) O(n):** Tree can become skewed.
- **Insert (Avg) O(log n):** Insert follows search path.
- **Insert (Worst) O(n):** Skewed tree degrades height.
- **Delete (Avg) O(log n):** Node removal follows search path.
- **Delete (Worst) O(n):** Re-linking in a skewed tree is linear.

---

### AVL Tree
- **Search (Avg/Worst) O(log n):** Tree is always height-balanced.
- **Insert (Avg/Worst) O(log n):** Rotations maintain balance.
- **Delete (Avg/Worst) O(log n):** Rebalancing preserves height.

---

### Red-Black Tree
- **Search (Avg/Worst) O(log n):** Height is bounded by rules.
- **Insert (Avg/Worst) O(log n):** Recoloring and rotations apply.
- **Delete (Avg/Worst) O(log n):** Properties are restored after removal.

---

### Heap
- **Access (Avg/Worst) O(1):** Root element is directly accessible.
- **Search (Avg/Worst) O(n):** Heap is not globally ordered.
- **Insert (Avg/Worst) O(log n):** Element bubbles up.
- **Delete (Avg/Worst) O(log n):** Heapify restores structure.

---

### Trie
- **L = String length**
- **Search (Avg/Worst) O(L):** Each character is visited once.
- **Insert (Avg/Worst) O(L):** Nodes are added per character.
- **Delete (Avg/Worst) O(L):** Characters are removed sequentially.

---

### Graph
- **V = Number of graph vertices**
- **E = Number of graph edges**
- **Search (Avg/Worst) O(V + E):** Traversal visits all vertices and edges.
- **Insert (Avg/Worst) O(1):** Nodes or edges are added directly.
- **Delete (Avg/Worst) O(V + E):** Related edges must be removed.

## Algorithm Time Complexity Explanations

### Linear Search
- **Best O(1):** Target is found at the first element.
- **Average O(n):** Elements are checked sequentially.
- **Worst O(n):** Target is last or not present.
- **Space O(1):** Uses a constant amount of extra memory.

---

### Binary Search
- **Best O(1):** Target is found at the middle immediately.
- **Average O(log n):** Search space halves each step.
- **Worst O(log n):** All divisions are required.
- **Space O(1):** Uses constant extra space.

---

### Bubble Sort
- **Best O(n):** Array is already sorted.
- **Average O(n²):** Adjacent elements are repeatedly swapped.
- **Worst O(n²):** Array is reverse sorted.
- **Space O(1):** Sorting is done in place.

---

### Selection Sort
- **Best O(n²):** Minimum search still scans entire array.
- **Average O(n²):** Repeated full scans are required.
- **Worst O(n²):** Behavior is consistent regardless of order.
- **Space O(1):** Sorting is done in place.

---

### Insertion Sort
- **Best O(n):** Array is already sorted.
- **Average O(n²):** Elements shift to make room.
- **Worst O(n²):** Array is reverse sorted.
- **Space O(1):** Sorting occurs in place.

---

### Merge Sort
- **Best O(n log n):** Array is always divided and merged.
- **Average O(n log n):** Consistent divide-and-conquer behavior.
- **Worst O(n log n):** Performance does not degrade.
- **Space O(n):** Extra arrays are required for merging.

---

### Quick Sort
- **Best O(n log n):** Pivot splits array evenly.
- **Average O(n log n):** Random pivots balance partitions.
- **Worst O(n²):** Poor pivot choice creates skewed partitions.
- **Space O(log n):** Recursive call stack grows with depth.
