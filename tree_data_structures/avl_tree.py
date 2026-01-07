# AVL Tree Data Structure Implementation in Python
# Use "python tree_data_structures/avl_tree.py" in the terminal to run this code

# Define a Node class for each node in the AVL tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


# Define an AVLTree class to manage the tree
class AVLTree:

    # Get the height of a node
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # Get the balance factor of a node
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotation
    def rotate_right(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # Left rotation
    def rotate_left(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Insert a value into the AVL tree
    def insert(self, node, value):

        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Left Left case
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # Right Right case
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # Left Right case
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left case
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # In-order traversal to print values in sorted order
    def inorder_traversal(self, node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.value)
        self.inorder_traversal(node.right)


# Create an AVL tree and insert values
tree = AVLTree()
root = None

values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = tree.insert(root, value)

print("In-order traversal of AVL tree:")
tree.inorder_traversal(root)
