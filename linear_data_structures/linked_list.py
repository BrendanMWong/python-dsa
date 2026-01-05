# Singly Linked List Implementation in Python
# Use "python linear_data_structures/linked_list.py" in the terminal to run this code

# Define a Node class to represent each element in the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Define a LinkedList class to manage the linked list
class LinkedList:

    # Initialize the linked list
    def __init__(self):
        self.head = None

    # Append a new node with the given value to the end of the list
    def append(self, value):
        new_node = Node(value)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the list and append the new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Print all values in the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()