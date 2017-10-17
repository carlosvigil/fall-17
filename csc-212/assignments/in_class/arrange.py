from Dequeue import Dequeue


def arrange(list_in):
    deq = Dequeue()
    list_out = []

    for elem in list_in:
        if elem >= 0:
            deq.add_front(elem)
        else:
            deq.add_rear(elem)
    while deq.size() > 0:
        list_out.append(deq.remove_rear())
    return list_out


def main():
    print(arrange([-3, 12, 6, -7, -1, 8]))


if __name__ == '__main__':
    main()
