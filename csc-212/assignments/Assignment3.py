"""Hi"""


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


class Hamburger:
    """The order slip at your local burger spot."""
    def __init__(self, weight=8, done='well', cheese=False, topp='lettuce'):
        self._weight = int(weight)
        self._doneness = done
        self._cheese = cheese
        # Toppings will be a list if user customizes their order
        self._toppings = topp

    def __str__(self):
        return ('{0._weight} oz\n'
                'Cooked {0._doneness}\n'
                'Cheese: {0._cheese}\n'
                'Toppings: {0._toppings}').format(self)

    def set_weight(self, weight):
        """Mutate the _weight attribute of the given instance, converting
        the input into an interger.
        """
        self._weight = int(weight)

    def get_weight(self):
        """Access the _weight attribute of the given instance, returning
        a string with ' oz' appended.
        """
        return self._weight

    def set_doneness(self, cook):
        """Mutate the _doneness attribute of the given instance."""
        self._doneness = cook

    def get_doneness(self):
        """Access the _doneness attribute of the given instance."""
        return self._doneness

    def set_cheese(self, cheese):
        """Mutate the _cheese attribute of the given instance."""
        self._cheese = cheese

    def get_cheese(self):
        """Access the _cheese attribute of the given instance."""
        return self._cheese

    def set_toppings(self, slip):
        """Mutate the _toppings attribute of the given instance, splitting a
        given string into a list.
        """
        self._toppings = slip.lower().split()

    def get_toppings(self):
        """Access the _toppings attribute of the given instance, joining each
        list element with a space.
        """
        return ' '.join(self._toppings)

    def bite(self):
        """Lessen the weight of the instantiated burger by one ounce."""
        if self._weight > 0:
            self._weight -= 1
            return True
        return False


def eat(order):
    """Lower the weight of the burger until it is gone."""
    print('Would you like to eat it?')
    if y_or_n():
        while order.bite():
            print('{} oz'.format(order.get_weight()))
    else:
        print('OK.')

    print('Would you like to order another burger?')
    return order_burger() if y_or_n() else print('Have a great day!')


def order_burger():
    """Aquire user input, decide how to instantiate a Hamburger class."""
    print('Welcome to Burger Place!')
    print('Would you like to customize your burger?')

    if y_or_n():
        print('How large would you like your burger?')
        ounces = input('Enter it in ounces: ')
        print('Great, thanks! Now, how well would you like your burger cooked?')
        cook_it = input('Enter here: ')
        print('OK. What about cheese?')
        cheese = y_or_n()
        print('Alright, now what toppings do you want?')
        topp = input('Enter each topping seperated by a space: ')

        custom_order = Hamburger(ounces, cook_it, cheese, topp)
        print('\nYour custom order...')
        print(custom_order)
        print()
        eat(custom_order)
    else:
        print('\nOK! One classic burger!')
        classic_order = Hamburger()
        print(classic_order)
        print()
        eat(classic_order)


def creds(day):
    """seal of origin; take day, output an assignment header."""
    print('\n# Carlos Vigil'
          '\n# A. Abd El-Raouf'
          '\n# CSC 212-02'
          '\n# {}\n'.format(day))


def main():
    """Runs the defined functions or methods."""
    creds('October 2, 2017')
    order_burger()


if __name__ == '__main__':
    main()
