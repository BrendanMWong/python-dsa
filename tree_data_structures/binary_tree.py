# Binary Tree Data Structure Implementation in Python
# Use "python tree_data_structures/binary_tree.py" in the terminal to run this code

# Define a Node class to represent each element in the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define a BinaryTree class to manage the binary tree structure
class BinaryTree:

    # Initialize the binary tree with a root node
    def __init__(self, root_value):
        self.root = Node(root_value)

    # Add a left child node to a given parent node
    def add_left(self, parent_node, child_value):
        new_node = Node(child_value)
        parent_node.left = new_node
        return new_node

    # Add a right child node to a given parent node
    def add_right(self, parent_node, child_value):
        new_node = Node(child_value)
        parent_node.right = new_node
        return new_node

    # Pre-order traversal: root to left to right
    def traverse_preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.traverse_preorder(node.left)
        self.traverse_preorder(node.right)

# Create root of the binary tree
tree = BinaryTree("root")

# Add left and right children to the root
left1 = tree.add_left(tree.root, "left1")
right1 = tree.add_right(tree.root, "right1")

# Add children to the left child of the root
tree.add_left(left1, "left1_left")
tree.add_right(left1, "left1_right")

# Traverse and print the binary tree in pre-order
tree.traverse_preorder(tree.root)
