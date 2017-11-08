"""Node class representing a node in a linked list
A node contains data and reference to the next node
Adopted from Section 3.9 in the textbook
"""


class Node:
    def __init__(self, init_data):
        """Create a Node object and initialize its data."""
        self.data = init_data
        self.next = None

    def get_data(self):
        """Accessor for node data"""
        return self.data

    def get_next(self):
        """Accessor for next reference"""
        return self.next

    def set_data(self, new_data):
        """Mutator for node data"""
        self.data = new_data

    def set_next(self, new_next):
        """Mutator for next reference"""
        self.next = new_next
