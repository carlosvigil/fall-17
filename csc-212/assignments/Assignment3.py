"""Hi"""


class Hamburger:
    """The order slip at your local burger spot.""" 
# TODO: add doc comments
    def __init__(self):
        self._weight = 0
        self._doneness = None
        self._cheese = bool
        self._toppings = []

    def __str__(self):
        return str(vars(self))

    def set_weight(self, weight):
    def get_weight(self):
        return self._weight

    def set_doneness(self, cooked):
    def get_doneness(self):
        return self._doneness

    def set_cheese(self, cheese):
    def get_cheese(self):
        return self._cheese

    def set_toppings(self):
    def get_toppings(self):
        return self._toppings

    def bite():
        if self._weight > 0:
            self._weight -= 1


def ask_for_burger():
    order = Hamburger()
    print('Welcome to Burger Place!\nHow large would you like your burger')
    ounces = input('Enter it in ounces: ')
    print('Great, thanks! Now, how well would you like your burger cooked?')
    cook_it = input('Enter here: ')
    print('OK. What about cheese?\n')
    cheese = input("Please enter 'True' or 'False': ")



def creds(day):
    """seal of origin; take day, output an assignment header."""
    print('\n# Carlos Vigil\n# A. Abd El-Raouf\n# CSC 212-02\n# %s\n' % (day))


def main():
    """Runs the defined functions or methods."""
    creds('October 1, 2017')
    yah = Hamburger()
    print(yah)


if __name__ == '__main__':
    main()
