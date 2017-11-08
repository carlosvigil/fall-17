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
        """Add an element to head of the list."""
        # Create a node using item as its data
        temp = Node(item)
        # make the next reference of the new node refer to the head
        # of the list
        temp.set_next(self.head)
        # modify the list head so that it references the new node
        self.head = temp

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
            elif data < item:
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
        return self.practical_search(item)[1]

    def size(self):
        """Returns the size of the list."""
        # start at the head of the list
        current = self.head
        count = 0
        # Traverse the list one element at a time.  We know
        # we reached the end when the next reference is None
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

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
    # create a list and add some elements to it
    aList = OrderedList()
    print("Adding 3, 5, and 8 to the list.")
    aList.add(3)
    aList.add(5)
    aList.add(8)

    print("List size:", aList.size())
    print("List content: ")
    aList.print_list()
    print('\nAssignment 6\n...for item 5\nIndex: ', end='')
    print(aList.index(5))
    print('Search: ', end='')
    print(aList.search(5))


if __name__ == "__main__":
    main()
