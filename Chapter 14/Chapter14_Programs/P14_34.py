class Employee:
    def __init__(self, name, password, salary):
        self._name = name
        self.password = password
        self.salary = salary

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


e = Employee('Jill', 'feb31', 5000)
print(e.name)
#e.name = 'Jack'

#print(e.password)
e.password = 'feb29'

e.salary = 6000
print(e.salary)

