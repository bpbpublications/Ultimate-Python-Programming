class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print('Hello I am', self.name)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def contact_details(self):
        print(self.address, self.phone)


class Employee(Person):
    pass


emp = Employee('Raghu', 30, 'D4, XYZ Street, Delhi', '994477291')
print(emp.name, emp.age, emp.address, emp.phone)
print(emp.is_adult())
emp.contact_details()

print(isinstance(emp, Employee), isinstance(emp, Person))

print(issubclass(Employee, Person))
