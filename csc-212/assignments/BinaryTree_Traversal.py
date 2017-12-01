'''
Implementation of the Binary Tree ADT defined in Section 6.4.2 
of the textbook (pdf version)
'''

class BinaryTree:
    '''
    Constructor initializes key to value provided (root).
    Left and right child references are None.  
    '''
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None
        
    '''
    Create new binary tree and insert it as left child of 
    current node.
    '''
    def insert_left(self, new_node):
        # if left child is None, create new node and modify 
        # the left reference
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        # otherise, create new node and modify the left 
        # reference of the current node so that it 
        # references new node
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
        
    '''
    Create new binary tree and insert it as right child of 
    current node.
    '''        
    def insert_right(self, new_node):
        # if there's no right child, create new node
        # and make it right child of current node
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        # otherise, create new node and modify the right 
        # reference of the current node so that it 
        # references new node
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
            
    '''
    Return right subtree
    '''    
    def get_right_child(self):
        return self.right_child
                
    '''
    Return left subtree
    '''
    def get_left_child(self):
        return self.left_child
         
    '''
    Modify the value of the current node
    '''       
    def set_root_val(self, obj):
        self.key = obj
     
    '''
    Get the value of the current node
    '''           
    def get_root_val(self):
        return self.key
    
   
# External implementations of tree traversal methods (i.e. Not
# part of the class definition).  Must be called with the tree
# reference as the argument.  
    
'''
Preorder tree traversal: Visit the root node first, then 
recursively do a preorder traversal of the left subtree, 
and finally a recursive preorder traversal of the right 
subtree.
'''
def preorder(tree):
    if tree:
        print(tree.get_root_val(), end = " ")
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

'''
Postorder tree traversal: Recursive postorder traversal of 
the left subtree, followed by a recursive postorder traversal 
of the right subtree, and finally visit the root.
'''
def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val(), end = " ")        

'''
Inorder tree traversal: Recursively do an inorder traversal 
of the left subtree, visit the root, and finally do a 
recursive inorder traversal of the right subtree.
'''
def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val(), end = " ")
        inorder(tree.get_right_child())


def main():      
    
    # Need to escape the backslash (with a backslash)
    print('''
        Creating the tree:
    
                 a
                / \\                
               b   c
              / \\   \\
             d   e   f
                /
               g
    
    ''')
    t = BinaryTree('a')
    t.insert_left('b')
    t.insert_right('c')
    t.get_left_child().insert_right('e')
    t.get_left_child().insert_left('d')
    t.get_left_child().get_right_child().insert_left('g')
    t.get_right_child().insert_right('f')
    
    print("Inorder traversal:")
    inorder(t)
    
    print("\n\nPreorder traversal:")
    preorder(t)
    
    print("\n\nPostorder traversal:")
    postorder(t)
    
    
    
    
if __name__ == "__main__":
    main()

