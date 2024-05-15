class Base:
    def method1(self):
        print('Base : method1 ')

    def method2(self):
        print('Base : method2 ')

    def method3(self):
        print('Base : method3 ')


class Derived(Base):

    def method2(self):
        print('Derived : method2 ')  # overriden method

    def method3(self):  # changed method
        super().method3()
        print('Derived : method3 ')


b = Base()
d = Derived()

b.method1()
b.method2()
b.method3()

d.method1()
d.method2()
d.method3()
