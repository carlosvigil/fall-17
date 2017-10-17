"""A class for stack applications; items are stored and removed in a
sequence.
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def view_all(self):
        print(self.items)

    def view_all_reversed(self):
        print([x for x in reversed(self.items)])


def main():
    """Runs tests on the defined functions."""
    s = Stack()

    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    s.view_all()
    s.view_all_reverse()

if __name__ == "__main__":
    main()
