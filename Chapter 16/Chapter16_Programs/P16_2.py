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

    def __init__(self, name, age, address, phone, salary, office_address, office_phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05


emp = Employee('Raghu', 30, 'D4, XYZ Street, Delhi', '994477291', 8000, 'ABC Street, Delhi', '897657888')
print(emp.name, emp.age, emp.address, emp.phone)
print(emp.office_address, emp.office_phone)

print(emp.is_adult())
emp.contact_details()
print(emp.calculate_tax())


