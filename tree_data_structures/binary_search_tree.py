# Binary Search Tree Data Structure Implementation in Python
# Use "python tree_data_structures/binary_search_tree.py" in the terminal to run this code

# Define a Node class to represent each element in the binary search tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define a BinarySearchTree class to manage the BST structure
class BinarySearchTree:

    # Initialize the BST with a root node
    def __init__(self, root_value):
        self.root = Node(root_value)

    # Insert a new value into the BST
    def insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(node.right, value)

    # Pre-order traversal: root to left to right
    def traverse_preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.traverse_preorder(node.left)
        self.traverse_preorder(node.right)

# Create root of the BST
bst = BinarySearchTree(10)

# Insert values into the BST
bst.insert(bst.root, 5)
bst.insert(bst.root, 15)
bst.insert(bst.root, 3)
bst.insert(bst.root, 7)
bst.insert(bst.root, 12)
bst.insert(bst.root, 18)

# Traverse and print the BST in pre-order
bst.traverse_preorder(bst.root)
