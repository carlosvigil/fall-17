"""As understood from Wikipedia and StackOverflow."""
import BinaryTree


def tree_sort(a_list):
    print('Tree sorting.')

    tree = BinaryTree.BinaryTree()
    tree.set_root_val(a_list[0])
    root = tree.get_root_val()

    for item in a_list:
        if not root:
            tree.set_root_val(item)
        # lesser to the left
        elif item < root:
            tree.insert_left(item)
        # greater to the right
        else:
            tree.insert_right(item)
