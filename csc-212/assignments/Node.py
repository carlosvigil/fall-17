# Node class representing a node in a linked list
# A node contains data and reference to the next node
# Adopted from Section 3.9 in the textbook

class Node:
    '''
    Create a Node object and initialize its data.  
    '''
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    '''
    Accessor for node data
    '''
    def get_data(self):
        return self.data
    
    '''
    Accessor for next reference
    '''
    def get_next(self):
        return self.next
    
    '''
    Mutator for node data
    '''
    def set_data(self, new_data):
            self.data = new_data
            
    '''
    Mutator for next reference
    '''
    def set_next(self, new_next):
            self.next = new_next    
            
