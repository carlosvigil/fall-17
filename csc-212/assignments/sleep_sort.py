
"""I was too tired to pay attention in class and still am so this assignment is
too hard, here is some humor. It sleeps for x in a list and prints x,
asynchronously. I didn't write this.
"""

import asyncio

async def __sleepsort_coro__(value, dest):
    await asyncio.sleep(value * 0.001) # Optimization!
    dest.append(value)

def sleepsort(unsorted):
    if not all((type(v) == int or type(v) == float for v in unsorted)):
        raise ValueError('all arguments must be numbers')

    if not all((v >= 0 for v in unsorted)):
        raise ValueError('all arguments must be non-negative')

    result = list()
    futures = set()
    for v in unsorted: futures.add(__sleepsort_coro__(v, result))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    return result

if __name__ == '__main__':
    source = [999, 3, 1.5, 0, 7, 7, 2, 5]
    print(source)
    print(sleepsort(source))
