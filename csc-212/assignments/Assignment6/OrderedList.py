"""Implementation of an ordered linked list ADT.
Adopted from Section 3.9 of the textbook.
"""

from Node import Node


class OrderedList:
    def __init__(self):
        """List is empty upon creation and the head reference is None."""
        self.head = None

    def is_empty(self):
        """Returns True if list is empty, False otherwise."""
        return self.head is None

    def add(self, item):
        """Add an `item` to the head of the list, maintaining value order."""
        # Create a temporary node using the item argument for the data param
        temp = Node(item)
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            # store items in an ascending order
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            # update the head
            temp.set_next(self.head)
            self.head = temp
        else:
            # insert the new node
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self, item):
        """Remove the first occurrence of parameter `item` from the list."""
        # keep track of current and previous elements
        current = self.head
        previous = None
        found = False
        # traverse the list
        while current is not None and not found:
            # when the node value matches the argument value stop searching
            if current.get_data() == item:
                found = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()
        if found:
            # when the node to be deleted is the head of the list
            if previous is None:
                self.head = current.get_next()
            # update references during a non-head node removal
            else:
                previous.set_next(current.get_next())

    def pop(self, pos=None):
        """Return and remove an item in the list, the last item if no `pos`
        argument is provided.
        """
        # empty check
        if self.head is None:
            return print('The list is empty.')
        else:
            current = self.head

        # Without argument: set iterator to pop the last item in the list
        if not pos:
            pos = self.size() - 1
        # reassign the head if position is the head
        if pos == 0:
            self.head = current.get_next()
        # traverse the list up to the position
        elif pos > 0:
            for node in range(pos):
                previous = current
                current = current.get_next()
            # update the previous node's reference
            previous.set_next(current.get_next())
        data = current.get_data()
        del current
        return data

    def replace(self, pos, data):
        """Given a position and a value, the method replaces the `data` of the
        node at the list position, where `pos` 0 corresponds to `self.head`.
        """
        # before proceeding check if there's anything in the list
        if not self.is_empty():
            # test if the given position is accessible
            if self.size() - 1 > pos < 0:
                return print('That position is out of range of the list size.')

            # iterate through the list until arriving at the given position
            current = self.head
            for node in range(pos):
                current = current.get_next()
            return current.set_data(data)

        print('This list is empty.')

    def practical_search(self, item):
        """Search for an `item` in the list; return in list node and `index`"""
        current = self.head
        found = False
        abort = False
        index = 0
        # search for the item
        while current is not None and not found and not abort:
            data = current.get_data()
            # stop if found
            if data == item:
                found = True
            # stop operation if the value has been passed
            elif data > item:
                abort = True
            # go to the next element
            else:
                index += 1
                current = current.get_next()
        if found:
            return [current, index]

    def search(self, item):
        """Search for an `item` in the list, return a boolean."""
        return True if self.practical_search(item) else False

    def index(self, item):
        """Return the index of a given `item` in the list."""
        if self.search(item):
            return self.practical_search(item)[1]
        print('{0}, not in the list.'.format(item))

    def size(self):
        """Returns the size of the list."""
        # start at the head of the list
        current = self.head
        count = 0
        # Traverse the list one element at a time.  We know
        # we reached the end when the next reference is None
        while current is not None:
            count += 1
            current = current.get_next()
        return count

        """Checks if the value is the only one in the list."""

    def duplicates(self):
        """Print the number of times a value is represented by a different
        node in the list.
        """
        if self.is_empty():
            print('The list is empty.')

        list_size = range(self.size())
        curr_node = self.head
        values = {}
        # traverse the list adding up a count of each value's appearance
        for node in list_size:
            curr_val = curr_node.get_data()
            next_node = curr_node.get_next()
            # start counting
            if curr_val in values:
                values[curr_val] += 1
            else:
                values[curr_val] = 1
            # move to the next
            if next_node is not None:
                curr_node = next_node
        # display results
        for val, count in values.items():
            print('{0} appears {1} time(s).'.format(val, count))

    def distinct_list(self):
        """Reduces the list to unique node values."""
        curr_node = self.head
        next_node = curr_node.get_next()

        while next_node is not None:
            curr_val = curr_node.get_data()
            next_val = next_node.get_data()
            # delete other nodes with identical values as the current one
            while curr_val == next_val:
                # load a node two steps over to reassign it as the next_node
                if next_node.get_next():
                    temp = next_node.get_next()
                    curr_node.set_next(temp)
                else:
                    del next_node
                    continue
                del next_node
                next_node = temp
                # reset the next_value
                next_val = next_node.get_data()
            # reached when all duplicates for a value have been deleted
            curr_node = next_node
            next_node = curr_node.get_next()

    def print_list(self):
        """Print a list of the node values."""
        if not self.is_empty():
            # collect the node values
            to_print = []
            current = self.head
            # traverse the list
            for node in range(self.size()):
                to_print.append(current.get_data())
                current = current.get_next()
            return print(to_print)
        return print('List is empty.')


def main():
    """Test defined class and methods."""
    linked_list = OrderedList()
    # add a random integer to the ordered list
    for num in range(15):
        linked_list.add(randint(1, 5))

    print('\nAssignment 6\n')
    print("List content: ")
    linked_list.print_list()

    # search and index methods
    if linked_list.search(3):
        print('...for item 3\n  Search: True')
        print('  Index: ', linked_list.index(3))
    elif linked_list.search(5):
        print('...for item 5\n  Search: True')
        print('  Index: ', linked_list.index(5))
    # pop method
    print('\nPop last item: ', linked_list.pop())
    print("List content: ")
    linked_list.print_list()
    print('Pop at position 1: ', linked_list.pop(1))
    print("List content: ")
    linked_list.print_list()
    linked_list.duplicates()
    # linked_list.distinct_list()
    # print("List content: ")
    # linked_list.print_list()


if __name__ == "__main__":
    from random import randint
    main()
