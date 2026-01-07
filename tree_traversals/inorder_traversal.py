# In-order Traversal of a Binary Search Tree in Python
# Use "python tree_traversals/inorder_traversal.py" to run this code

# Node class for BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BST class with insert method
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

    # In-order traversal: left → root → right
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)


# Example usage
bst = BST()
for value in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(value)

print("In-order traversal:")
bst.inorder(bst.root)
