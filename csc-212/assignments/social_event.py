"""Number 2 of Assignment 3"""
from reuse import creds, y_or_n

class SocialEvent:
    """Creates an event with a title, date, and attendee number."""
    def __init__(self):
        """Create an instance of the class."""
        self._title = ''
        self._date = ''
        self._peeps = 0

    def __str__(self):
        """Print the attributes of the instance."""
        title = self._title.title()
        return '{1}\nDate: {0._date}\npeeps: {0._peeps}'.format(self, title)

    def set_title(self, title):
        """Mutate the title of the event instance."""
        self._title = title

    def get_title(self):
        """Access the title attribute of the instance."""
        return self._title

    def set_date(self, date):
        """Mutate the date of the event instance."""
        self._date = date

    def get_date(self):
        """Access the date attribute of the instance."""
        return self._date

    def set_peeps(self, peeps):
        """Mutate the peeps (attendees) of the event instance."""
        self._peeps = int(peeps)

    def get_peeps(self):
        """Access the peeps (attendees) attribute of the instance."""
        return self._peeps

def ask_for_five():
    """Input 5 SocialEvent instances."""
    events = {}
    for num in range(5):
        events[num] = (SocialEvent())
        print('Event {}'.format(num + 1))
        events[num].set_title(input('Enter an event title: '))
        events[num].set_date(input('Enter the event\'s date: '))
        events[num].set_peeps(input('Enter the number of attendees: '))
    return events

def sort_attendees(events):
    """Sort the events by the number of attendees."""
    by_attendees = sorted(events, key=SocialEvent: get_peeps())

    for num in range(5):
        print(by_attendees[num - 1])

def main():
    """Run program to test the class and its methods."""
    creds('October 3, 2017')
    sort_attendees(ask_for_five())


if __name__ == '__main__':
    main()
