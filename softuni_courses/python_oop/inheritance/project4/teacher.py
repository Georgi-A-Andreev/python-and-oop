from project4.employee import Employee
from project4.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'