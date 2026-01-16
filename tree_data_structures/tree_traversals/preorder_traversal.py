# Pre-order Traversal of a Binary Search Tree in Python
# Use "python tree_data_structures/tree_traversals/preorder_traversal.py" to run this code

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

    # Pre-order traversal: root → left → right
    def preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)


bst = BST()
for value in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(value)

print("Pre-order traversal:")
bst.preorder(bst.root)
