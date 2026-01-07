# Heap Data Structure Implementation in Python
# Use "python tree_data_structures/heap.py" in the terminal to run this code

# Define a MaxHeap class to maintain a max-heap
class MaxHeap:
    
    # Initialize an empty heap
    def __init__(self):
        self.heap = []

    # Insert a new value into the heap
    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    # Restore heap property after insertion
    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    # Remove and return the maximum value from the heap
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return max_value

    # Restore heap property after extraction
    def _bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)

    # Print the current heap array
    def print_heap(self):
        print(self.heap)


# Define a MinHeap class to maintain a min-heap
class MinHeap:
    
    # Initialize an empty heap
    def __init__(self):
        self.heap = []

    # Insert a new value into the heap
    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    # Restore heap property after insertion
    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    # Remove and return the minimum value from the heap
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_value

    # Restore heap property after extraction
    def _bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    # Print the current heap array
    def print_heap(self):
        print(self.heap)


# Example usage for MaxHeap
print("MAX HEAP")
max_heap = MaxHeap()
for value in [10, 20, 5, 30, 25]:
    max_heap.insert(value)

print("Heap after inserts:")
max_heap.print_heap()

print("Extract max:", max_heap.extract_max())
print("Heap after extracting max:")
max_heap.print_heap()


# Example usage for MinHeap
print("\nMIN HEAP")
min_heap = MinHeap()
for value in [10, 20, 5, 30, 25]:
    min_heap.insert(value)

print("Heap after inserts:")
min_heap.print_heap()

print("Extract min:", min_heap.extract_min())
print("Heap after extracting min:")
min_heap.print_heap()
