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


def main():

    r = BinaryTree('a')
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val('hello')
    print(r.get_right_child().get_root_val())


if __name__ == "__main__":
    main()
