"""Implementation of an ordered list ADT as a linked list.
Adopted from Section 3.9 of the textbook.
"""

from Node import Node


class OrderedList:
    """List is empty upon creation and the head reference is None."""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Returns True if list is empty, False otherwise."""
        return self.head is None

    def add(self, item):
        """Add an element to head of the list, maintaining value order."""
        # Create a node using item as its data
        temp = Node(item)
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            # make the next reference of the new node refer to the head
            # of the list
            temp.set_next(self.head)
            # modify the list head so that it references the new node
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self, item):
        """Remove the first occurrence of item from the list."""
        # keep track of current and previous elements
        current = self.head
        previous = None
        found = False
        # traverse the list
        while current is not None and not found:
            # if we have a match, stop
            if current.get_data() == item:
                found = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()

        # the element to be deleted is the head of the list
        if found:
            if previous is None:
                self.head = current.get_next()
            # the element to be deleted is not the head
            else:
                previous.set_next(current.get_next())

    def pop(self, pos=None):
        if self.head is None:
            return print('The list is empty.')

        current = self.head
        # Without argument: set iterator to pop the last item in the list
        if pos is None:
            pos = self.size() - 1
        # access the position in the list
        # reassign the head if position is head
        if pos == 0:
            self.head = current.get_next()
        elif pos > 0:
            for node in range(pos):
                previous = current
                current = current.get_next()
            # update previous node's reference
            previous.set_next(current.get_next())
        data = current.get_data()
        del current
        return data

    def replace(self, pos, val):
        """Given a position, and a value, the method replaces the value of the
        element at the position, where position 0 corresponds to the head of
        the list with the new value.
        """
        # before proceeding check if there's anything in the list
        if not self.is_empty():
            # test if the given position is accessible
            if self.size() - 1 > pos < 0:
                return print('That position is out of range of the list size.')

            current = self.head
            # iterate through the list until arriving at the given position
            for node in range(pos):
                current = current.get_next()
            return current.set_data(val)

        print('This list is empty.')

    def practical_search(self, item):
        """Search for an item in the list, return node and index."""
        current = self.head
        found = False
        abort = False
        index = 0
        # As long as the element is not found, nor search aborted, and haven't
        # reached the end of the list
        while current is not None and not found and not abort:
            data = current.get_data()
            if data == item:
                found = True
            # stop operation if the value has been passed
            elif data > item:
                abort = True
            # go to the next element
            else:
                index += 1
                current = current.get_next()
        return [current, index] if found else None

    def search(self, item):
        """Search for an item in the list, return a boolean."""
        return True if self.practical_search(item) else False

    def index(self, item):
        """Return the index of a given item in the list."""
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

    def duplicates(self):
        curr_node = self.head

        for index in range(5):
            # assign current and next values
            curr_val = curr_node.get_data()
            if curr_node.get_next() is not None:
                next_node = curr_node.get_next()
                next_val = next_node.get_data()
            count = 1
            stop = False

            # check the next value
            while curr_val == next_val and not stop:
                count += 1
                # reassign current and next shifting one index over in the list
                curr_node = next_node
                curr_val = next_val
                if curr_node.get_next() is not None:
                    next_node = curr_node.get_next()
                    next_val = next_node.get_data()
                else:
                    stop = True

            print('{0} appears {1} time(s) in the list.'.format(curr_val, count))
            curr_node = next_node

    def list_distinct(self):
        pass

    def print_list(self):
        """Print a list of the node values."""
        if not self.is_empty():
            to_print = []
            current = self.head

            for node in range(self.size()):
                to_print.append(current.get_data())
                current = current.get_next()
        else:
            return print('List is empty.')
        print(to_print)


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


if __name__ == "__main__":
    from random import randint
    main()
