# Python DSA

A collection of Python implementations of common data structures and algorithms, organized by category for reference.

## Table of Contents

- [Time Complexity Tables](#time-complexity)
- [Data Structure Explanations](#data-structure-time-complexity-explanations)
- [Algorithm Explanations](#algorithm-time-complexity-explanations)

## Time Complexity

For these tables, operations are based on the intended use of the data structure. Access is N/A for data structures that don't support indexing. 

| Data Structure     | Access (Avg) | Access (Worst) | Search (Avg) | Search (Worst) | Insert (Avg) | Insert (Worst) | Delete (Avg) | Delete (Worst) |
| ------------------ | ------------ | -------------- | ------------ | -------------- | ------------ | -------------- | ------------ | -------------- |
| Array / List       | [O(1)](#array-list-access) | [O(1)](#array-list-access) | [O(n)](#array-list-search) | [O(n)](#array-list-search) | [O(n)](#array-list-insert) | [O(n)](#array-list-insert) | [O(n)](#array-list-delete) | [O(n)](#array-list-delete) |
| Linked List        | N/A | N/A | [O(n)](#linked-list-search) | [O(n)](#linked-list-search) | [O(1)](#linked-list-insert) | [O(1)](#linked-list-insert) | [O(1)](#linked-list-delete) | [O(1)](#linked-list-delete) |
| Stack              | N/A | N/A | [O(n)](#stack-search) | [O(n)](#stack-search) | [O(1)](#stack-insert) | [O(1)](#stack-insert) | [O(1)](#stack-delete) | [O(1)](#stack-delete) |
| Queue              | N/A | N/A | [O(n)](#queue-search) | [O(n)](#queue-search) | [O(1)](#queue-insert) | [O(1)](#queue-insert) | [O(1)](#queue-delete) | [O(1)](#queue-delete) |
| Deque              | N/A | N/A | [O(n)](#deque-search) | [O(n)](#deque-search) | [O(1)](#deque-insert) | [O(1)](#deque-insert) | [O(1)](#deque-delete) | [O(1)](#deque-delete) |
| String             | [O(1)](#string-access) | [O(1)](#string-access) | [O(n)](#string-search) | [O(n)](#string-search) | [O(n)](#string-insert) | [O(n)](#string-insert) | [O(n)](#string-delete) | [O(n)](#string-delete) |
| Hash Table (Dict)  | [O(1)](#hash-table-access) | [O(n)](#hash-table-access) | [O(1)](#hash-table-search) | [O(n)](#hash-table-search) | [O(1)](#hash-table-insert) | [O(n)](#hash-table-insert) | [O(1)](#hash-table-delete) | [O(n)](#hash-table-delete) |
| Hash Set           | [O(1)](#hash-set-access) | [O(n)](#hash-set-access) | [O(1)](#hash-set-search) | [O(n)](#hash-set-search) | [O(1)](#hash-set-insert) | [O(n)](#hash-set-insert) | [O(1)](#hash-set-delete) | [O(n)](#hash-set-delete) |
| Binary Tree        | N/A | N/A | [O(n)](#binary-tree-search) | [O(n)](#binary-tree-search) | [O(n)](#binary-tree-insert) | [O(n)](#binary-tree-insert) | [O(n)](#binary-tree-delete) | [O(n)](#binary-tree-delete) |
| Binary Search Tree | N/A | N/A | [O(log n)](#bst-search) | [O(n)](#bst-search) | [O(log n)](#bst-insert) | [O(n)](#bst-insert) | [O(log n)](#bst-delete) | [O(n)](#bst-delete) |
| AVL Tree           | N/A | N/A | [O(log n)](#avl-search) | [O(log n)](#avl-search) | [O(log n)](#avl-insert) | [O(log n)](#avl-insert) | [O(log n)](#avl-delete) | [O(log n)](#avl-delete) |
| Red-Black Tree     | N/A | N/A | [O(log n)](#rbt-search) | [O(log n)](#rbt-search) | [O(log n)](#rbt-insert) | [O(log n)](#rbt-insert) | [O(log n)](#rbt-delete) | [O(log n)](#rbt-delete) |
| Heap               | [O(1)](#heap-access) | [O(1)](#heap-access) | [O(n)](#heap-search) | [O(n)](#heap-search) | [O(log n)](#heap-insert) | [O(log n)](#heap-insert) | [O(log n)](#heap-delete) | [O(log n)](#heap-delete) |
| Trie               | N/A | N/A | [O(L)](#trie-search) | [O(L)](#trie-search) | [O(L)](#trie-insert) | [O(L)](#trie-insert) | [O(L)](#trie-delete) | [O(L)](#trie-delete) |
| Graph              | N/A | N/A | [O(V+E)](#graph-search) | [O(V+E)](#graph-search) | [O(1)](#graph-insert) | [O(1)](#graph-insert) | [O(V+E)](#graph-delete) | [O(V+E)](#graph-delete) |

| Algorithm           | Best Case | Average Case | Worst Case | Space Complexity |
|--------------------|-----------|--------------|------------|----------------|
| Linear Search       | [O(1)](#linear-search-best) | [O(n)](#linear-search-average) | [O(n)](#linear-search-worst) | [O(1)](#linear-search-space) |
| Binary Search       | [O(1)](#binary-search-best) | [O(log n)](#binary-search-average) | [O(log n)](#binary-search-worst) | [O(1)](#binary-search-space) |
| Bubble Sort         | [O(n)](#bubble-sort-best) | [O(n²)](#bubble-sort-average) | [O(n²)](#bubble-sort-worst) | [O(1)](#bubble-sort-space) |
| Selection Sort      | [O(n²)](#selection-sort-best) | [O(n²)](#selection-sort-average) | [O(n²)](#selection-sort-worst) | [O(1)](#selection-sort-space) |
| Insertion Sort      | [O(n)](#insertion-sort-best) | [O(n²)](#insertion-sort-average) | [O(n²)](#insertion-sort-worst) | [O(1)](#insertion-sort-space) |
| Merge Sort          | [O(n log n)](#merge-sort-best) | [O(n log n)](#merge-sort-average) | [O(n log n)](#merge-sort-worst) | [O(n)](#merge-sort-space) |
| Quick Sort          | [O(n log n)](#quick-sort-best) | [O(n log n)](#quick-sort-average) | [O(n²)](#quick-sort-worst) | [O(log n)](#quick-sort-space) |

## Data Structure Time Complexity Explanations

### Array / List
<a id="array-list-access"></a>
- **Access (Avg/Worst) O(1):** Indexing jumps directly to the memory address.
<a id="array-list-search"></a>
- **Search (Avg/Worst) O(n):** Elements must be checked sequentially.
<a id="array-list-insert"></a>
- **Insert (Avg/Worst) O(n):** Elements may need to be shifted.
<a id="array-list-delete"></a>
- **Delete (Avg/Worst) O(n):** Removing an element shifts following items.

### Linked List
<a id="linked-list-search"></a>
- **Search (Avg/Worst) O(n):** Nodes must be traversed one by one.
<a id="linked-list-insert"></a>
- **Insert (Avg/Worst) O(1):** Pointer updates take constant time.
<a id="linked-list-delete"></a>
- **Delete (Avg/Worst) O(1):** Node removal only changes links.

### Stack
<a id="stack-search"></a>
- **Search (Avg/Worst) O(n):** Elements must be popped to inspect.
<a id="stack-insert"></a>
- **Insert (Avg/Worst) O(1):** Push adds to the top.
<a id="stack-delete"></a>
- **Delete (Avg/Worst) O(1):** Pop removes the top element.

### Queue
<a id="queue-search"></a>
- **Search (Avg/Worst) O(n):** Elements must be dequeued to inspect.
<a id="queue-insert"></a>
- **Insert (Avg/Worst) O(1):** Enqueue adds to the rear.
<a id="queue-delete"></a>
- **Delete (Avg/Worst) O(1):** Dequeue removes from the front.

### Deque
<a id="deque-search"></a>
- **Search (Avg/Worst) O(n):** Elements must be traversed.
<a id="deque-insert"></a>
- **Insert (Avg/Worst) O(1):** Items can be added at either end.
<a id="deque-delete"></a>
- **Delete (Avg/Worst) O(1):** Items can be removed at either end.

### String
<a id="string-access"></a>
- **Access (Avg/Worst) O(1):** Characters are indexable.
<a id="string-search"></a>
- **Search (Avg/Worst) O(n):** Characters must be scanned.
<a id="string-insert"></a>
- **Insert (Avg/Worst) O(n):** A new string must be created.
<a id="string-delete"></a>
- **Delete (Avg/Worst) O(n):** Characters are copied or shifted.

### Hash Table (Dictionary)
<a id="hash-table-access"></a>
- **Access (Avg) O(1):** Hashing locates the bucket quickly.
- **Access (Worst) O(n):** All keys collide into one bucket.
<a id="hash-table-search"></a>
- **Search (Avg) O(1):** Hash lookup is constant time.
- **Search (Worst) O(n):** Collision chains must be scanned.
<a id="hash-table-insert"></a>
- **Insert (Avg) O(1):** Key is placed using its hash.
- **Insert (Worst) O(n):** Rehashing or collisions degrade performance.
<a id="hash-table-delete"></a>
- **Delete (Avg) O(1):** Key is found via hashing.
- **Delete (Worst) O(n):** Collision chains must be searched.

### Hash Set
<a id="hash-set-access"></a>
- **Access (Avg) O(1):** Hashing locates the element.
- **Access (Worst) O(n):** All elements collide.
<a id="hash-set-search"></a>
- **Search (Avg) O(1):** Hash lookup is constant.
- **Search (Worst) O(n):** Collisions force linear scan.
<a id="hash-set-insert"></a>
- **Insert (Avg) O(1):** Element is hashed and placed.
- **Insert (Worst) O(n):** Rehashing or collisions occur.
<a id="hash-set-delete"></a>
- **Delete (Avg) O(1):** Element is hash-located.
- **Delete (Worst) O(n):** Collision resolution is required.

### Binary Tree (Unordered)
<a id="binary-tree-search"></a>
- **Search (Avg/Worst) O(n):** Tree may require full traversal.
<a id="binary-tree-insert"></a>
- **Insert (Avg/Worst) O(n):** Finding a position takes traversal.
<a id="binary-tree-delete"></a>
- **Delete (Avg/Worst) O(n):** Node must be located first.

### Binary Search Tree (Unbalanced)
<a id="bst-search"></a>
- **Search (Avg) O(log n):** Tree height is logarithmic on average.
- **Search (Worst) O(n):** Tree can become skewed.
<a id="bst-insert"></a>
- **Insert (Avg) O(log n):** Insert follows search path.
- **Insert (Worst) O(n):** Skewed tree degrades height.
<a id="bst-delete"></a>
- **Delete (Avg) O(log n):** Node removal follows search path.
- **Delete (Worst) O(n):** Re-linking in a skewed tree is linear.

### AVL Tree
<a id="avl-search"></a>
- **Search (Avg/Worst) O(log n):** Tree is always height-balanced.
<a id="avl-insert"></a>
- **Insert (Avg/Worst) O(log n):** Rotations maintain balance.
<a id="avl-delete"></a>
- **Delete (Avg/Worst) O(log n):** Rebalancing preserves height.

### Red-Black Tree
<a id="rbt-search"></a>
- **Search (Avg/Worst) O(log n):** Height is bounded by rules.
<a id="rbt-insert"></a>
- **Insert (Avg/Worst) O(log n):** Recoloring and rotations apply.
<a id="rbt-delete"></a>
- **Delete (Avg/Worst) O(log n):** Properties are restored after removal.

### Heap
<a id="heap-access"></a>
- **Access (Avg/Worst) O(1):** Root element is directly accessible.
<a id="heap-search"></a>
- **Search (Avg/Worst) O(n):** Heap is not globally ordered.
<a id="heap-insert"></a>
- **Insert (Avg/Worst) O(log n):** Element bubbles up.
<a id="heap-delete"></a>
- **Delete (Avg/Worst) O(log n):** Heapify restores structure.

### Trie
<a id="trie-search"></a>
- **Search (Avg/Worst) O(L):** Each character is visited once.
<a id="trie-insert"></a>
- **Insert (Avg/Worst) O(L):** Nodes are added per character.
<a id="trie-delete"></a>
- **Delete (Avg/Worst) O(L):** Characters are removed sequentially.

### Graph
<a id="graph-search"></a>
- **Search (Avg/Worst) O(V + E):** Traversal visits all vertices and edges.
<a id="graph-insert"></a>
- **Insert (Avg/Worst) O(1):** Nodes or edges are added directly.
<a id="graph-delete"></a>
- **Delete (Avg/Worst) O(V + E):** Related edges must be removed.

## Algorithm Time Complexity Explanations

### Linear Search
<a id="linear-search-best"></a>
- **Best O(1):** Target is found at the first element.
<a id="linear-search-average"></a>
- **Average O(n):** Elements are checked sequentially.
<a id="linear-search-worst"></a>
- **Worst O(n):** Target is last or not present.
<a id="linear-search-space"></a>
- **Space O(1):** Uses a constant amount of extra memory.

### Binary Search
<a id="binary-search-best"></a>
- **Best O(1):** Target is found at the middle immediately.
<a id="binary-search-average"></a>
- **Average O(log n):** Search space halves each step.
<a id="binary-search-worst"></a>
- **Worst O(log n):** All divisions are required.
<a id="binary-search-space"></a>
- **Space O(1):** Uses constant extra space.

### Bubble Sort
<a id="bubble-sort-best"></a>
- **Best O(n):** Array is already sorted.
<a id="bubble-sort-average"></a>
- **Average O(n²):** Adjacent elements are repeatedly swapped.
<a id="bubble-sort-worst"></a>
- **Worst O(n²):** Array is reverse sorted.
<a id="bubble-sort-space"></a>
- **Space O(1):** Sorting is done in place.

### Selection Sort
<a id="selection-sort-best"></a>
- **Best O(n²):** Minimum search still scans entire array.
<a id="selection-sort-average"></a>
- **Average O(n²):** Repeated full scans are required.
<a id="selection-sort-worst"></a>
- **Worst O(n²):** Behavior is consistent regardless of order.
<a id="selection-sort-space"></a>
- **Space O(1):** Sorting is done in place.

### Insertion Sort
<a id="insertion-sort-best"></a>
- **Best O(n):** Array is already sorted.
<a id="insertion-sort-average"></a>
- **Average O(n²):** Elements shift to make room.
<a id="insertion-sort-worst"></a>
- **Worst O(n²):** Array is reverse sorted.
<a id="insertion-sort-space"></a>
- **Space O(1):** Sorting occurs in place.

### Merge Sort
<a id="merge-sort-best"></a>
- **Best O(n log n):** Array is always divided and merged.
<a id="merge-sort-average"></a>
- **Average O(n log n):** Consistent divide-and-conquer behavior.
<a id="merge-sort-worst"></a>
- **Worst O(n log n):** Performance does not degrade.
<a id="merge-sort-space"></a>
- **Space O(n):** Extra arrays are required for merging.

### Quick Sort
<a id="quick-sort-best"></a>
- **Best O(n log n):** Pivot splits array evenly.
<a id="quick-sort-average"></a>
- **Average O(n log n):** Random pivots balance partitions.
<a id="quick-sort-worst"></a>
- **Worst O(n²):** Poor pivot choice creates skewed partitions.
<a id="quick-sort-space"></a>
- **Space O(log n):** Recursive call stack grows with depth.
