""" Hi """


def creds(day):
    """seal of origin; take day, output an assignment header."""
    print('\n# Carlos Vigil\n# A. Abd El-Raouf\n# CSC 212-02\n# %s\n' % (day))


def censor_program():
    """Opens an existing file and returns a new one with all 4 letter words
    censored by '****'.
    """
    try:
        fout = open('alice_censor.txt', 'w')
    except:
        print('Error on opening file to write.')

    with open('alice.txt') as fin:
        for line in fin:
            for word in line.split():
                if len(word) == 4:
                    fout.write('**** ')
                else:
                    fout.write(word + ' ')
            fout.write('\n')
    fout.close()
    # print(open('alice_censor.txt').read())


def histogram(text):
    """Receives text, outputs the occurance of each english letter."""
    letters = {}

    for char in text:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters


def note():
    """Compares two character dictionaries, returning false if the latter has
    less of one char present in the former.
    """
    nicety = histogram(input('Hey there, type and enter a message here.\n'))
    magazine = histogram(input('Now, enter the text from a magazine.\n'))
    status = True

    for key in nicety:
        if key not in magazine:
            status = False
            break
        elif nicety[key] > magazine[key]:
            status = False
            break
    print(status)
    return status


def main():
    """Run all programs."""
    creds('September 16, 2016')
    print('Assignment 2 - Exercise 1:\n')
    censor_program()
    print('censor_program() has executed.')
    print('Read alice_censor, i.e., `less alice_censor.txt`.')
    print('\n- Exercise 2:\n')
    note()

if __name__ == '__main__':
    main()
