""" Hello """


def creds(day):
    """seal of origin; take day, output an assignment header."""
    print('\n# Carlos Vigil\n# A. Abd El-Raouf\n# CSC 212-02\n# %s\n' % (day))


def right_justify(val):
    """Return a given value with added space to end on line 70."""
    str_val = str(val)
    empty_spaces = 70
    space_to_print = empty_spaces - len(str_val)
    result = ' ' * space_to_print + str_val
    return result


def formatted_ouput():
    """Print a right-adjusted list of numbers."""
    nums = [1.0, 10.0, 100.0, 1000.0, 10000.0]
    for val in nums:
        print(right_justify(val))


def lists_and_list_comprehensions():
    """Using list comprehensions add all even numbers to 1000."""
    # print(sum(range(0, 1000, 2)))
    uhm = [x for x in range(1000) if not x % 2]
    okay = 0
    for val in uhm:
        okay += val
    print(okay)


def cartesian_distance(x1_, y1_, x2_, y2_):
    """In-class exercise to find the distance between 2 points"""
    dx_ = x2_ - x1_  # find distance through subtracting x and y respectively
    dy_ = y2_ - y1_
    return print('distance x is', dx_, '\ndistance y is', dy_)


# Runs the defined functions of this file
def main():
    """Run all functions in this file (with some added commentary)"""
    creds('September 7, 2017')
    print('\nThus, Assignment 1 – Exercise 1:')
    formatted_ouput()
    print('\nAssignment 1 – Exercise 2:')
    lists_and_list_comprehensions()
    # Extra unnecessary
    print('\nExtra:\n')
    print('cartesian_distance(40, 50, 81, 11)')
    cartesian_distance(40, 50, 81, 11)
    print("\nright_justify('allo')\n", right_justify('allo'))


if __name__ == '__main__':
    main()
