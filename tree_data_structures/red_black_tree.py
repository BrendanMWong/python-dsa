# Red-Black Tree Data Structure Implementation in Python
# Use "python tree_data_structures/red_black_tree.py" in the terminal to run this code

RED = "RED"
BLACK = "BLACK"

# Define a Node class for each node in the Red-Black Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None


# Define a RedBlackTree class to manage the tree
class RedBlackTree:

    def __init__(self):
        self.nil = Node(None)
        self.nil.color = BLACK
        self.root = self.nil

    # Left rotation
    def rotate_left(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # Right rotation
    def rotate_right(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.nil:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    # Insert a new value into the tree
    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.nil
        new_node.right = self.nil

        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = RED
        self.fix_insert(new_node)

    # Fix Red-Black Tree violations after insert
    def fix_insert(self, node):
        while node.parent and node.parent.color == RED:

            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_right(node.parent.parent)

            else:
                uncle = node.parent.parent.left

                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_left(node.parent.parent)

        self.root.color = BLACK

    # In-order traversal
    def inorder_traversal(self, node):
        if node == self.nil:
            return
        self.inorder_traversal(node.left)
        print(node.value, node.color)
        self.inorder_traversal(node.right)


# Create a Red-Black Tree and insert values
tree = RedBlackTree()

values = [10, 20, 30, 15, 25, 5, 1]

for value in values:
    tree.insert(value)

print("In-order traversal of Red-Black Tree:")
tree.inorder_traversal(tree.root)
