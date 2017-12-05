import random
import time


def timer():
    elapsed = 0
    size = 0
    size_inc = 10000
    print('')

    while elapsed < 60:
        size += size_inc
        ints = [random.randrange(0, size) for x in range(size)]

        start = time.perf_counter()
        //
        end = time.perf_counter()
        elapsed = end - start

        print(size, '\t{0:.5f}'.format(elapsed, 'sec.\n'))
