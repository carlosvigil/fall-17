"""Creates hamburgers and eats them really fast."""
from reuse import creds, y_or_n

class Hamburger:
    """The order slip at your local burger spot."""
    def __init__(self):
        self._weight = 8
        self._doneness = 'medium'
        self._cheese = False
        self._toppings = ['lettuce']

    def __str__(self):
        tstr = ' '.join(self._toppings)
        return ('{0._weight} oz\n'
                'Cooked {0._doneness}\n'
                'Cheese: {0._cheese}\n'
                'Toppings: {1}').format(self, tstr)

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
        self._toppings = slip.lower().split(' ')

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
    order = Hamburger()
    print('Would you like to customize your burger?')

    if y_or_n():
        print('How large would you like your burger?')
        order.set_weight(input('Enter it in ounces: '))
        print('Great, thanks! How well would you like your burger cooked?')
        order.set_doneness(input('Enter here: '))
        print('OK. What about cheese?')
        order.set_cheese(y_or_n())
        print('Alright, now what toppings do you want?')
        order.set_toppings(input('Enter each topping seperated by a space: '))
        print('\nYour custom order...')
    else:
        print('\nOK! One classic burger!')

    print(order)
    print()
    eat(order)


def main():
    """Runs the defined functions or methods."""
    creds('October 2, 2017')
    print('Welcome to Burger Place!')
    order_burger()


if __name__ == '__main__':
    main()
