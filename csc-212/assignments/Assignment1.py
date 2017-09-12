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


def strings():
    """Ask for user input and return result of a text search."""
    user_text = str(input(
        'Type some text here, then press enter.\n')).lower()
    user_word = str(input(
        'Enter a word to search for in the text entered.\n')).lower()
    index = 0
    results = []
    if user_word not in user_text:
        print('The entered word was not found in the text.')
        return
    # store the positive results of each search, stop when there are none
    while user_word in user_text[index:len(user_text)] and index >= 0:
        finder = user_text.find(user_word, index, len(user_text))
        index = finder + len(user_word)
        results.append(finder)
    print('Word found at the following indexes of your entered text:')
    print(results)


def lists_and_inputs():
    """Ask for a sequence of words, then, display unique words."""
    words = []
    new_word = ''
    print('Enter a series of words, pressing enter after each.',
          '\n(Press enter twice if done)\n')
    print('incomplete; sleep is important')
    # while True:
    #     new_word = str(input('New word:\n')).lower()
    #     if len(new_word) > 0:
    #         words.append(new_word)
    #     else:
    #         continue
    # unique = [x for x in words if (words.pop(words.index(x)) )]
    # for w in words:
    #     first = words.find(w)
    #     words.pop(first)


def cartesian_distance(x1_, y1_, x2_, y2_):
    """In-class exercise to find the distance between 2 points."""
    dx_ = x2_ - x1_  # find distance through subtracting x and y respectively
    dy_ = y2_ - y1_
    return print('distance x is', dx_, '\ndistance y is', dy_)


# Runs the defined functions of this file
def main():
    """Run all functions in this file (with some added commentary)"""
    creds('September 11, 2017')
    print('\nThus, Assignment 1 – Exercise 1:')
    formatted_ouput()
    print('\nAssignment 1 – Exercise 2:')
    lists_and_list_comprehensions()
    print('\n*** Exercise 3 ***')
    strings()
    print('\n...and exercise 4')
    lists_and_inputs()
    # Extra unnecessary
    print('\nExtra:')
    print('cartesian_distance(40, 50, 81, 11)')
    cartesian_distance(40, 50, 81, 11)
    print("\nright_justify('allo')\n", right_justify('allo'))


if __name__ == '__main__':
    main()
