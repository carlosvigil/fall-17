import time
import random
import bubble_sort
import selection_sort
import merge_sort
# import tree_sort


def time_binary_search():
    elapsed = 0
    size = 0
    size_inc = 10000
    print('')

    while elapsed < 60:
        size += size_inc
        ints = [random.randrange(0, size) for x in range(size)]

        start = time.perf_counter()
        bubble_sort.bubble_sort(ints)
        end = time.perf_counter()
        elapsed = end - start

        print(size, '\t{0:.5f}'.format(elapsed, 'sec.\n'))


def time_selection_search():
    elapsed = 0
    size = 0
    size_inc = 10000
    print('')

    while elapsed < 60:
        size += size_inc
        ints = [random.randrange(0, size) for x in range(size)]

        start = time.perf_counter()
        selection_sort.selection_sort(ints)
        end = time.perf_counter()
        elapsed = end - start

        print(size, '\t{0:.5f}'.format(elapsed, 'sec.\n'))


def time_merge_search():
    elapsed = 0
    size = 0
    size_inc = 10000
    print('')

    while elapsed < 60:
        size += size_inc
        ints = [random.randrange(0, size) for x in range(size)]

        start = time.perf_counter()
        merge_sort.merge_sort(ints)
        end = time.perf_counter()
        elapsed = end - start

        print(size, '\t{0:.5f}'.format(elapsed, 'sec.\n'))


def main():
    time_selection_search()
    time_binary_search()
    time_merge_search()


if __name__ == '__main__':
    main()
