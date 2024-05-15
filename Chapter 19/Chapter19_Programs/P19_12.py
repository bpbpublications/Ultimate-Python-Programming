class Employee:
    def __init__(self, name, phone, basic, ta, da):
        self.name = name
        self.phone = phone
        self.basic = basic
        self.ta = ta
        self.da = da

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return f'{self.name} {self.phone} {self.basic} {self.ta} {self.da}'

    def __repr__(self):
        return f'{self.name} {self.phone} {self.basic} {self.ta} {self.da}'


e1 = Employee('Zeba', 89889444, 3000, 500, 200)
e2 = Employee('Amit', 99883994, 4000, 300, 500)
e3 = Employee('Neema', 83988399, 3000, 1000, 500)
e4 = Employee('Rini', 99878784, 3500, 0, 500)

L = [e1, e2, e3, e4]
print(L)
L.sort()
print(L)

L = [e1, e2, e3, e4]
print(L)
L.sort(key=lambda e: e.basic + e.ta + e.da)
print(L)
