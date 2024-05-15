from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def contact_details(self):
        print(self.name, self.phone)

    @abstractmethod
    def compute_salary(self):
        pass


class PartTimeEmployee(Employee):
    def __init__(self, name, phone, hours):
        super().__init__(name, phone)
        self.hours = hours

    def compute_salary(self):
        print('Calculating salary of part time employee')


class FullTimeEmployee(Employee):
    def compute_salary(self):
        print('Calculating salary of full time employee')


class TemporaryEmployee(Employee):
    def compute_salary(self):
        print('Calculating salary of temporary employee')


e1 = PartTimeEmployee('Jack', 999909090, 4)
e2 = FullTimeEmployee('Jim', 989898989)
e3 = TemporaryEmployee('John', 789898989)

employees = [e1, e2, e3]

for e in employees:
    e.contact_details()
    e.compute_salary()
