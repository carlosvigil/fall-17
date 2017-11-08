def pali(string):

    if len(string) > 1 and string[0] == string[-1]:
        return True
    elif len(string) == 1:
        return True
    else:
        return False

    return pali(string[1:-1])

