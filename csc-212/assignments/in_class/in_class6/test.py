def add_it(nums):
    total = 0
    for num in nums:
        total += num
    return total


def add_re(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + add_re(nums[1:])


if __name__ == '__main__':
    from timeit import timeit

    setup = "from __main__ import add_it, add_re"
    print(timeit('add_it(range(10))', setup=setup))
    print(timeit('add_re(range(10))', setup=setup))
