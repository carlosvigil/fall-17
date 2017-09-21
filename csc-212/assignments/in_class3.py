"""Hi"""


class Student:
    """Represents a learning participant of a course.

    attributes: name, attend, grades
    """

    def __init__(self, _name='', _attend=0, _grades=''):
        """Instantiates the object with relative blanks for the fields of
        the student's name, attendance, and grades.
        """
        self._name = _name
        self._attend = _attend
        self._grades = list(_grades)

    def set_name(self, name):
        """Mutates the _name attribute of the Student instance."""
        self._name = name

    def get_name(self):
        """Retrieves the _name attribute of the Student instance."""
        return self._name

    def attend(self):
        """Mutates the _attend field, incrementing its integer by +1."""
        self._attend += 1

    def get_attend(self):
        """Accesses the _attend field, returning its current value."""
        return self._attend

    def add_grade(self, grade):
        """Append a new grade value to the field of grades."""
        self._grades.append(grade)

    def get_grades(self):
        """Accesses the _grades field, returning its current values."""
        return self._grades


def main():
    """Calls the functions and methods defined in this file."""
    allen = Student()
    allen.set_name("Allen Minium")
    allen.attend()
    allen.add_grade(100)
    print(allen)
    print(allen.get_name())
    print(allen.get_attend())
    print(allen.get_grades())


if __name__ == '__main__':
    main()
