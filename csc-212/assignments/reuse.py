"""Oft reused code."""

def creds(day):
    """seal of origin; take day, output an assignment header."""
    print('\n# Carlos Vigil'
          '\n# A. Abd El-Raouf'
          '\n# CSC 212-02'
          '\n# {}\n'.format(day))


def y_or_n():
    """Accept a yes or no answer, then, return a corresponding boolean."""
    answer = ''
    yup = answer == 'yes' or answer == 'y'
    nope = answer == 'no' or answer == 'n'

    while not yup or not nope:
        answer = input("Type 'yes' or 'no': ").lower()
        yup = answer == 'yes' or answer == 'y'
        nope = answer == 'no' or answer == 'n'

        if yup:
            return True
        elif nope:
            return False
        else:
            print('Error, please try again.')
