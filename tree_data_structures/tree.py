# Tree Data Structure Implementation in Python
# Use "python tree_data_structures/tree.py" in the terminal to run this

# Define a Node class to represent each element in the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

# Define a Tree class to manage the tree structure
class Tree:

    # Initialize the tree with a root node
    def __init__(self, root_value):
        self.root = Node(root_value)

    # Add a child node to a given parent node
    def add_child(self, parent_node, child_value):
        new_node = Node(child_value)
        parent_node.children.append(new_node)
        return new_node

    # Traverse the tree and print each node's value
    def traverse(self, node):
        print(node.value)
        for child in node.children:
            self.traverse(child)

# Create root of the tree
tree = Tree("root")

# Add children to the root
child1 = tree.add_child(tree.root, "child1")
child2 = tree.add_child(tree.root, "child2")

# Add children to one of the children
tree.add_child(child1, "grandchild1")
tree.add_child(child1, "grandchild2")

# Traverse and print the tree
tree.traverse(tree.root)
