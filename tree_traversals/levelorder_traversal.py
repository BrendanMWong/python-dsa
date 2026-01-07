# Level-order (Breadth-First) Traversal of a Binary Search Tree in Python
# Use "python tree_traversals/levelorder_traversal.py" to run this code

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    # Level-order traversal using a queue
    def levelorder(self, node):
        if node is None:
            return
        queue = deque()
        queue.append(node)
        while queue:
            current = queue.popleft()
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


bst = BST()
for value in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(value)

print("Level-order traversal:")
bst.levelorder(bst.root)
