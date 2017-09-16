"""In-class assignment 9/14, makes a histogram from user inputted string"""


def histo():
    """Receives text from the user, outputs the occurance of each english
       letter
    """
    the_text = input('enter some text, preferably more than 1.\n')
    the_letters = {}
    for char in the_text:
        if char in the_letters:
            the_letters[char] += 1
        else:
            the_letters[char] = 1
    print(the_letters)


def main():
    """RUN"""
    histo()

if __name__ == '__main__':
    main()
