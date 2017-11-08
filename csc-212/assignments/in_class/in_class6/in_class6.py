"""In-class recursion exercises."""


def count_down(num):
    """Given a value n, the function prints the value n and count down printing
    (n-1),…till it prints 0.
    """
    return print(num) if num == 0 else (print(num), count_down(num-1))


def backwards_alphabet(letter):
    """Given an alphabet letter, the function prints the letter and all previous
    letters till it prints a.  (consider all lower-case letters)
    """
    num = ord(letter)
    pre_num = num - 1
    pre_letter = chr(pre_num)

    print(letter, end=' ')
    if num > 97:
        backwards_alphabet(pre_letter)


def factorial(num):
    """Given an integer n, the function should calculate the factorial of n
    according to the fomula:
        factorial(n)=n*(n-1)*(n-2)…*1
        Given that factorial(1)=1
    """
    return factorial(num-1) * num if num > 1 else num


def main():
    """Test defined functions."""
    count_down(5)
    backwards_alphabet('t')
    print()
    for num in range(10):
        print(factorial(num))


if __name__ == '__main__':
    main()
