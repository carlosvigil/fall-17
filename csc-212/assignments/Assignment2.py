""" Hi """


def creds(day):
    """seal of origin; take day, output an assignment header."""
    print('\n# Carlos Vigil\n# A. Abd El-Raouf\n# CSC 212-02\n# %s\n' % (day))


def censor_program():
    """Opens an existing file and returns a new one with all 4 letter words
    censored by '****'.
    """
    fout = open('alice_censor.txt', 'w')
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


def main():
    """Run all programs."""
    creds('September 16, 2016')
    censor_program()

if __name__ == '__main__':
    main()
